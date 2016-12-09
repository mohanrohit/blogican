#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
current_directory = os.getcwd()

SITENAME = u"Pelican"
SITEURL = ''
RELATIVE_URLS = True

STATIC_PATHS = ["static"]

AUTHOR = u'Rohit Mohan'

IGNORE_FILES = [
  "tech/web-development-with-python-and-flask/*",
  "tech/pyflask/*",
  "tech/pygae/*",
  "tech/web-development-with-python-and-flask/backup/*",
  "tech/web-development-with-python-and-gae/*"
]

SUMMARY_MAX_LENGTH = 50

# theming

THEME = current_directory + "/theme/pelican-bootstrap3-custom"

BOOTSTRAP_THEME = "journal"
PYGMENTS_STYLE = "vs"
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False

PLUGIN_PATHS = [current_directory + "/plugins"]
PLUGINS = ["series", "series_list"]

DISPLAY_SERIES_ON_SIDEBAR = True
SHOW_SERIES = False
SERIES_TEXT = "" #"Part <strong>%(index)s</strong> of the <strong>%(name)s</strong> series"

DISPLAY_ALL_SERIES_ON_SIDEBAR = True

SHOW_ARTICLE_AUTHOR = True

# end theming

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DRAFT_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}'
DRAFT_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

LOAD_CONTENT_CACHE = True
