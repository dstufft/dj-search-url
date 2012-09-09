DJ-SEARCH-URL
===============

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``SEARCH_URL`` environment variable to configure your Haystack application.


Usage
-----

Configure your Search index in ``settings.py`` from ``SEARCH_URL``::

    HAYSTACK_CONNECTIONS = {"default": dj_search_url.conf()}

Parse an arbitrary Database URL::

    HAYSTACK_CONNECTIONS = {"default": dj_search_url.conf("elasticsearch://..")}

Installation
------------

Installation is simple too::

    $ pip install dj-search-url
