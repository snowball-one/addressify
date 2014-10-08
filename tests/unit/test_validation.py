# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from addressify.client import Client
from addressify.exceptions import InvalidApiKeyError, InvalidStateError


def test_cannot_create_client_with_malformed_api_key():
    with pytest.raises(InvalidApiKeyError):
        Client(api_key="invalid_value")


def test_can_create_client_with_well_formed_api_key():
    try:
        Client(api_key="11111111-1111-1111-1111-111111111111")
    except InvalidApiKeyError:
        pytest.fail("InvalidApiKeyError raise for well formed key")


def test_validate_state_raises_exception_for_invalid_state():
    client = Client(api_key="11111111-1111-1111-1111-111111111111")
    with pytest.raises(InvalidStateError):
        client._validate_state('nowhere')


def test_validate_state_passes_for_none_state():
    client = Client(api_key="11111111-1111-1111-1111-111111111111")
    try:
        client._validate_state(None)
    except InvalidStateError:
        pytest.fail("InvalidStateError raised for None")


def test_validate_states_passes_for_valid_states():
    client = Client(api_key="11111111-1111-1111-1111-111111111111")
    for state in client.VALID_STATES:
        try:
            client._validate_state(state)
        except InvalidStateError:
            pytest.fail("InvalidStateError raised for {}".format(state))
