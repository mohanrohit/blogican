#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = os.environ.get("PELICAN_SITEURL") or "" # 'http://localhost:8000' <-- "ip-address:port"
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_RSS = "feeds/rss.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"

TAG_FEED_RSS = "tag/%s/feed/rss.xml"

CATEGORY_FEED_RSS = "category/%s/feed/rss.xml"

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

DISQUS_SITENAME = "rohits-pensieve"
#GOOGLE_ANALYTICS = ""
