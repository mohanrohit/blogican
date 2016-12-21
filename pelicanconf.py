#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
current_directory = os.getcwd()

SITENAME = u"Pelican"
SITEURL = ''
RELATIVE_URLS = True

DATE_FORMATS = {
  "en": "%Y %b %d"
}

STATIC_PATHS = ["static", "images"]

AUTHOR = u'Rohit Mohan'

SUMMARY_MAX_LENGTH = 50

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

# broken in Pelican for tag generation
# PAGINATION_PATTERNS = (
  # (1, "{base_name}/", "{base_name}/index.html"),
  # (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
# )

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
SHOW_SERIES = True
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

ARTICLE_URL = "{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}"
ARTICLE_SAVE_AS = "{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"

DRAFT_URL = "{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}"
DRAFT_SAVE_AS = "{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"

PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "pages/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"
TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORIESS_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"

AUTHOR_URL = "author/{slug}"
AUTHOR_SAVE_AS = "author/{slug}/index.html"
AUTHORS_URL = "authors/"
AUTHORS_SAVE_AS = "authors/index.html"

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
