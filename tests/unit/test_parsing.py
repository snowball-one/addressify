# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from addressify.client import Address


def test_json_parsed_to_address_object():
    data = {"Number": "680", "Street": "GEORGE", "StreetType": "ST",
            "Suburb": "SYDNEY", "StreetSuffix": None, "State": "NSW",
            "StreetLine": "680 GEORGE ST", "UnitType": None,
            "UnitNumber": None, "Postcode": "2000"}
    address = Address.from_json(data)
    assert address.number == data['Number']
    assert address.street == data['Street']
    assert address.street_type == data['StreetType']
    assert address.suburb == data['Suburb']
    assert address.street_suffix == data['StreetSuffix']
    assert address.state == data['State']
    assert address.street_line == data['StreetLine']
    assert address.unit_type == data['UnitType']
    assert address.unit_number == data['UnitNumber']
    assert address.postcode == data['Postcode']
