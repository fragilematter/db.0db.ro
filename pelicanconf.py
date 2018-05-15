#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')

AUTHOR = 'Doru Barbu'
SITENAME = 'db.0db.ro'
SITEURL = 'https://db.0db.ro'

PATH = 'content'
TIMEZONE = 'Europe/Bucharest'
DEFAULT_LANG = 'EN'
THEME = 'pelican-blueidea'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# menu
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('blog', '/category/blog.html'),
    ('radio', '/category/radio.html'),
    ('archive', '/category/archive.html'),
    ('about', '/pages/about.html'),
    )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
  ('cc-by-sa 4.0', 'http://creativecommons.org/licenses/by-sa/4.0/'),
)

# Social widget
SOCIAL = (
  ('github', 'https://github.com/fragilematter'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ['rst_html5_audiovideo']
STATIC_PATHS = ['images', 'downloads']
