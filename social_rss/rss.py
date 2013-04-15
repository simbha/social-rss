"""Generates an RSS."""

import os
import re

import xml.sax.saxutils

import tornado.httputil
import tornado.template

from social_rss import config


TEMPLATE_LOADER = tornado.template.Loader(os.path.dirname(__file__), autoescape=None)
"""Template loader."""


def generate(feed):
    """Generates an RSS."""

    rss =  TEMPLATE_LOADER.load("rss.rss").generate(
        feed=feed, date=tornado.httputil.format_timestamp,
        escape=xml.sax.saxutils.escape)

    if not config.DEBUG_MODE:
        rss = re.sub(br">\s+<", b"><", rss)

    return rss
