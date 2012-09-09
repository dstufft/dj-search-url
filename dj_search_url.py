# -*- coding: utf-8 -*-

import os

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


# Register database schemes in URLs.
urlparse.uses_netloc.append("elasticsearch")
urlparse.uses_netloc.append("solr")
urlparse.uses_netloc.append("whoosh")
urlparse.uses_netloc.append("simple")


DEFAULT_ENV = "SEARCH_URL"

SCHEMES = {
    "elasticsearch": "haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine",
    "solr": "haystack.backends.solr_backend.SolrEngine",
    "whoosh": "haystack.backends.whoosh_backend.WhooshEngine",
    "simple": "haystack.backends.simple_backend.SimpleEngine",
}

USES_URL = ["solr"]
USES_INDEX = ["elasticsearch"]
USES_PATH = ["whoosh"]


def config(env=DEFAULT_ENV, default=None):
    """Returns configured HAYSTACK_CONNECTIONS dictionary from ``env``."""

    config = {}

    s = os.environ.get(env, default)

    if s:
        config = parse(s)

    return config


def parse(url):
    """Parses a search URL."""

    config = {}

    url = urlparse.urlparse(url)

    # Remove query strings.
    path = url.path[1:]
    path = path.split('?', 2)[0]

    if url.scheme in SCHEMES:
        config["ENGINE"] = SCHEMES[url.scheme]

    if url.scheme in USES_URL:
        config["URL"] = urlparse.urlunparse(("http",) + url[1:])

    if url.scheme in USES_INDEX:
        if path.endswith("/"):
            path = path[:-1]

        split = path.rsplit("/", 1)

        if len(split) > 1:
            path = split[:-1]
            index = split[-1]
        else:
            path = ""
            index = split[0]

        config.update({
            "URL": urlparse.urlunparse(("http",) + url[1:2] + (path,) + url[3:]),
            "INDEX_NAME": index,
        })

    if url.scheme in USES_PATH:
        config.update({
            "PATH": path,
        })

    return config
