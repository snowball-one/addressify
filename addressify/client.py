# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import re
import requests

from .exceptions import InvalidStateError, InvalidApiKeyError


class Client(object):

    BASE_URL = 'http://api.addressify.com.au'
    GUID_REGEX = re.compile(r"^[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$")

    VALID_STATES = ('NSW', 'ACT', 'VIC', 'QLD', 'SA', 'WA', 'NT', 'TAS')

    def __init__(self, api_key, max_results=10):
        if self.GUID_REGEX.match(api_key) is None:
            raise InvalidApiKeyError("Invalid api_key")
        self._api_key = api_key
        self.max_results = max_results

    def _validate_state(self, state):
        if state is not None and state not in self.VALID_STATES:
            raise InvalidStateError("{0} is not a valid state".format(state))

    def _make_request(self, path, params={}):
        params['api_key'] = self._api_key
        url = "{0}{1}".format(self.BASE_URL, path)
        params = dict(filter(lambda x: x[1] != None, params.iteritems()))
        try:
            return requests.get(url, params=params).json()
        except requests.HTTPError:
            return None

    def auto_complete(self, term, state=None, postcode=None, max_results=None):
        """
        Gets a list of addresses that begin with the given term.
        """
        self._validate_state(state)
        params = {"term": term, "state": state, "postcode": postcode,
                  "max_results": max_results or self.max_results}
        return self._make_request('/address/autoComplete', params)

    def address_line_auto_complete(self, term, state=None, postcode=None,
                                   max_results=None):
        """
        Gets a list of address lines that begin with the given term.
        """
        self._validate_state(state)
        params = {"term": term, "state": state, "postcode": postcode,
                  "max_results": max_results or self.max_results}
        return self._make_request('/address/addressLineAutoComplete', params)

    def suburb_auto_complete(self, term, state=None, postcode=None,
                             max_results=None):
        """
        Gets a list of suburbs that begin with the given term.
        """
        self._validate_state(state)
        params = {"term": term, "state": state, "postcode": postcode,
                  "max_results": max_results or self.max_results}
        return self._make_request('/address/suburbAutoComplete', params)

    def suburb_state_postcode_auto_complete(self, term, state=None,
                                            postcode=None, max_results=None):
        """
        Gets a list of suburbs and postcodes where the suburb begins with the
        given term.
        """
        self._validate_state(state)
        params = {"term": term, "state": state, "postcode": postcode,
                  "max_results": max_results or self.max_results}
        return self._make_request('/address/suburbStatePostcodeAutoComplete',
                                  params)

    def suburbs_for_postcode(self, postcode):
        """
        Gets a list of suburbs for the given postcode.
        """
        params = {"term": postcode}
        return self._make_request('/address/getSuburbsforPostcode', params)

    def state_for_postcode(self, postcode):
        """
        Gets the state in which the given postcode is located..
        """
        params = {"term": postcode}
        return self._make_request('/address/getStateforPostcode', params)

    def parse_address(self, address_line):
        """
        Parses the given address into it's individual address fields.
        """
        params = {"term": address_line}
        json = self._make_request('/address/getParsedAddress', params)
        if json is None:
            return None
        return Address.from_json(json)

    def similar(self, address_line, max_results=None):
        """
        Gets a list of valid addresses that are similar to the given term, can
        be used to match invalid addresses to valid addresses.
        """
        params = {"term": address_line,
                  "max_results": max_results or self.max_results}
        return self._make_request('/address/getSimilar', params)

    def is_valid(self, address_line):
        """
        Checks whether the given address is valid. Please note that validation
        is only performed on the street, suburb, state and postcode. Street and
        unit numbers are not checked for validity.
        """
        params = {"term": address_line}
        return self._make_request('/address/validate', params)

    def daily_call_count(self):
        """
        Gets the current daily API call count for your account. This counter
        will reset at midnight AEST. When this counter reaches the daily API
        call limit for your account type all other Addressify API calls will
        fail until the counter resets. Will return -1 if the api_key does not
        exist.
        """
        return self._make_request('/account/getDailyAPICallCount')


class Address(object):

    def __init__(self, unit_number, unit_type, number, street, street_type,
                 street_suffix, street_line, suburb, state, postcode):
        """
        Simple address object which is nicer than json dict with nasty
        pascal-case names
        """
        self.unit_number = unit_number
        self.number = number
        self.unit_type = unit_type
        self.street = street
        self.street_type = street_type
        self.street_suffix = street_suffix
        self.street_line = street_line
        self.suburb = suburb
        self.state = state
        self.postcode = postcode

    @classmethod
    def from_json(cls, json):
        return cls(
            json.get('UnitNumber'),
            json.get('UnitType'),
            json.get('Number'),

            json.get('Street'),
            json.get('StreetType'),
            json.get('StreetSuffix'),
            json.get('StreetLine'),

            json.get('Suburb'),
            json.get('State'),

            json.get('Postcode'),
        )
