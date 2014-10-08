# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mock import Mock, patch

from addressify.client import Client, Address


API_KEY = "11111111-1111-1111-1111-111111111111"


def mock_requests(r, response=None):
    result = Mock()
    result.to_json = Mock(return_value=response)
    r.get = Mock(return_value=result)


def test_make_request_appends_api_key():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client._make_request('/a/path')
        requests.get.assert_called_with('http://api.addressify.com.au/a/path',
                                        params={'api_key': API_KEY})


def test_simple_auto_complete():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.auto_complete(term="109/175 Sturt Street")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/autoComplete',
            params={'api_key': API_KEY, 'term': "109/175 Sturt Street",
                    "max_results": 10}
        )


def test_auto_complete_with_postcode():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.auto_complete(term="109/175 Sturt Street", postcode="3006")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/autoComplete',
            params={'api_key': API_KEY, 'term': "109/175 Sturt Street",
                    "max_results": 10, "postcode": "3006"}
        )


def test_address_line_auto_complete():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.address_line_auto_complete(term="109/175 Sturt Street")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/addressLineAutoComplete',
            params={'api_key': API_KEY, 'term': "109/175 Sturt Street",
                    "max_results": 10}
        )


def test_suburb_auto_complete():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.suburb_auto_complete(term="southbank")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/suburbAutoComplete',
            params={'api_key': API_KEY, 'term': "southbank",
                    "max_results": 10}
        )


def test_suburb_state_postcode_auto_complete():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.suburb_state_postcode_auto_complete(term="southbank")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/suburbStatePostcodeAutoComplete',  # noqa
            params={'api_key': API_KEY, 'term': "southbank",
                    "max_results": 10}
        )


def test_suburb_for_postcode():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.suburbs_for_postcode(postcode="3006")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/getSuburbsforPostcode',
            params={'api_key': API_KEY, 'term': "3006"}
        )


def test_state_for_postcode():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.state_for_postcode(postcode="3006")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/getStateforPostcode',
            params={'api_key': API_KEY, 'term': "3006"}
        )


def test_parse_address():
    data = {"Number": "680", "Street": "GEORGE", "StreetType": "ST",
            "Suburb": "SYDNEY", "StreetSuffix": None, "State": "NSW",
            "StreetLine": "680 GEORGE ST", "UnitType": None,
            "UnitNumber": None, "Postcode": "2000"}
    with patch('addressify.client.requests') as requests:
        mock_requests(requests, data)
        client = Client(api_key=API_KEY)
        address = client.parse_address(
            address_line="109/175 Sturt Street, SOUTH BANK, VIC 3182")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/getParsedAddress',
            params={
                'api_key': API_KEY,
                'term': "109/175 Sturt Street, SOUTH BANK, VIC 3182"}
        )
        assert isinstance(address, Address)


def test_similar():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.similar(
            address_line="109/175 Sturt Street, SOUTH BANK, VIC 3182")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/getSimilar',
            params={
                'api_key': API_KEY,
                'term': "109/175 Sturt Street, SOUTH BANK, VIC 3182",
                'max_results': 10}
        )


def test_is_valid():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.is_valid(
            address_line="109/175 Sturt Street, SOUTH BANK, VIC 3182")
        requests.get.assert_called_with(
            'http://api.addressify.com.au/address/validate',
            params={
                'api_key': API_KEY,
                'term': "109/175 Sturt Street, SOUTH BANK, VIC 3182"}
        )


def test_daily_call_count():
    with patch('addressify.client.requests') as requests:
        mock_requests(requests)
        client = Client(api_key=API_KEY)
        client.daily_call_count()
        requests.get.assert_called_with(
            'http://api.addressify.com.au/account/getDailyAPICallCount',
            params={'api_key': API_KEY}
        )
