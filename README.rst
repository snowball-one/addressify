Addressify Python Client
========================

.. image:: https://travis-ci.org/snowball-one/addressify.svg
    :target: https://travis-ci.org/snowball-one/addressify


This is a simply Python client for the `addressify.com.au`_ API.

*"Addressify is a cloud based web API that allows web site, web application and
desktop application developers to easily implement free address verification,
validation, checking, parsing and autocomplete for Australia in their
applications."*

.. _addressify.com.au: http://www.addressify.com.au

Installation
------------

Since the Python addressify client has not yet been released to pypi, you will
need to install it from git. This can still be done using pip::

    pip install git+https://github.com/snowball-one/addressify.git



Usage Quickstart
----------------

The Addressify Python client currently covers all the available api calls of
`addressify.com.au`_. e.g.:

.. code-block:: Python
    from addressify import Client

    client = Client(your_api_key)
    results = client.auto_complete('109/175 Sturt Street, SOUTH')


API Calls Available
-------------------

client.auto_complete
++++++++++++++++++++

Gets a list of addresses that begin with the given term.

Arguments:

term (Required)
   The start of an address.

state (Optional)
   The state to search for addresses in. ('NSW', 'ACT', 'VIC', 'QLD', 'SA',
   'WA', 'NT', 'TAS')

postcode (Optional)
   The postcode to search for addresses in.

max_results (Optional)
   The maximum number of results to return (minumum: 1, maximum: 20,
   default: 10).


Example Response::

    [
        "1 GEORGE ST, TAHMOOR NSW 2573",
        "1 GEORGE ST, TELARAH NSW 2320",
        "1 GEORGE ST, TEMORA NSW 2666",
        "1 GEORGE ST, TENTERFIELD NSW 2372",
        "1 GEORGE ST, THE ROCKS NSW 2000"
    ]


client.address_line_auto_complete
+++++++++++++++++++++++++++++++++

Gets a list of address lines that begin with the given term.

Arguments:

term (Required)
   The start of an address line.

state (Optional)
   The state to search for addresses in. ('NSW', 'ACT', 'VIC', 'QLD', 'SA',
   'WA', 'NT', 'TAS')

postcode (Optional)
   The postcode to search for addresses in.

max_results (Optional)
   The maximum number of results to return (minumum: 1, maximum: 20,
   default: 10).

Example Response::

    [
        "1 GEORDIE ST",
        "1 GEORGANN ST",
        "1 GEORGE AVE",
        "1 GEORGE CL",
        "1 GEORGE CRES"
    ]

client.suburb_auto_complete
++++++++++++++++++++++++++++

Gets a list of suburbs that begin with the given term.

Arguments:

term (Required)
   The start of a suburb name

state (Optional)
   The state to search for addresses in. ('NSW', 'ACT', 'VIC', 'QLD', 'SA',
   'WA', 'NT', 'TAS')

postcode (Optional)
   The postcode to search for addresses in.

max_results (Optional)
   The maximum number of results to return (minumum: 1, maximum: 20,
   default: 10).

Example Response::

    [
        "SUFFOLK PARK",
        "SUGARLOAF",
        "SUMMER HILL",
        "SUMMER HILL CREEK",
        "SUMMER ISLAND"
    ]

client.suburb_state_postcode_auto_complete
++++++++++++++++++++++++++++++++++++++++++

Gets a list of suburbs and postcodes where the suburb begins with the given
term.

Arguments:

term (Required)
   The start of a suburb name.

state (Optional)
   The state to search for addresses in. ('NSW', 'ACT', 'VIC', 'QLD', 'SA',
   'WA', 'NT', 'TAS')

postcode (Optional)
   The postcode to search for addresses in.

max_results (Optional)
   The maximum number of results to return (minumum: 1, maximum: 20,
   default: 10).


Example Response::

    [
        "SUMMER HILL, NSW 2130",
        "SUMMER HILL, NSW 2421",
        "SUMMER HILL CREEK, NSW 2800",
        "SUMMER ISLAND, NSW 2440",
        "SUMMERHILL, TAS 7250"
    ]

client.suburbs_for_postcode
+++++++++++++++++++++++++++

Gets a list of suburbs for the given postcode.

Arguments:

postcode (Required)
   The postcode.


Example Response::

    [
        "BARANGAROO, NSW 2000",
        "DAWES POINT, NSW 2000",
        "HAYMARKET, NSW 2000",
        "MILLERS POINT, NSW 2000",
        "SYDNEY, NSW 2000",
        "SYDNEY SOUTH, NSW 2000",
        "THE ROCKS, NSW 2000"
    ]

client.state_for_postcode
+++++++++++++++++++++++++

Gets the state in which the given postcode is located.

Arguments:

postcode (Required)
   The postcode.

Example Response::
    "NSW"


client.parse_address
++++++++++++++++++++

Parses the given address into it's individual address fields.

Arguments:

address_line (Required)
   The address to parse.

Example Response::

    addressify.client.Address(
        number="680",
        street="GEORGE",
        street_type="ST",
        suburb="SYDNEY",
        street_suffix=None,
        state="NSW",
        street_line="680 GEORGE ST",
        unit_type=None
        unit_number=None,
        postcode="2000"
    )

client.get_similar
++++++++++++++++++

Gets a list of valid addresses that are similar to the given term, can be used
to match invalid addresses to valid addresses.

Arguments:

address_line (Required)
   The address to find similar addresses for

max_results (Optional)
   The maximum number of results to return (minumum: 1, maximum: 10,
   default: 10).

Example Response::

    [
        "1 GEORGE ST, SYDNEY NSW 2000"
    ]

client.validate
+++++++++++++++

Checks whether the given address is valid. Please note that validation is only
performed on the street, suburb, state and postcode. Street and unit numbers
are not checked for validity.

Arguments

address_line (Required)
   The address to validate.

Example Response::
    true

client.daily_call_count
+++++++++++++++++++++++

Gets the current daily API call count for your account. This counter will reset
at midnight AEST. When this counter reaches the daily API call limit for your
account type all other Addressify API calls will fail until the counter resets.

Will return -1 if the api_key does not exist.

Example Response::
    1000
