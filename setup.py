#!/usr/bin/env python
"""
DJ-Search-URL
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
"""
from setuptools import setup

setup(
    name="dj-searchurl",
    version="0.1",

    description="Use Search URLs in your Django Haystack Application.",
    long_description=__doc__,
    url="https://github.com/dstufft/dj-search-url",

    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",

    extras_require={
        "tests": ["pytest"],
    },

    py_modules=["dj_search_url"],
    include_package_data=True,

    zip_safe=False,
)
