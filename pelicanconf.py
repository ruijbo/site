from __future__ import unicode_literals
import datetime
import os
import subprocess

# General settings
AUTHOR = 'Rui J. Oliveira'
SITENAME = AUTHOR
SRCURL = 'https://github.com/ruijbo/site'

SITEURL = 'http://home.uevora.pt/~ruio'

# Path settings
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
STATIC_PATHS = ['static', 'paper', 'javascript']
TIMEZONE = 'Europe/Lisbon'
SLUGIFY_SOURCE = 'basename'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
DIRECT_TEMPLATES = ()
ARTICLE_EXCLUDES = ['javascript']

EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_LANG = 'en'

MENUITEMS = (('Home', ''),
         ('Education', 'education'),
         ('Experience', 'experience'),
         ('Affiliations', 'affiliations'),
         ('Contact', 'contact'),
         )

PLUGIN_PATHS = ['plugins']
PLUGINS = ['html_rst_directive', 'icons']

# Social widget
SOCIAL = (
    ('google-scholar', 'https://scholar.google.com/citations?user=NCfDM3YAAAAJ&hl=en'),
    ('researchgate', 'https://www.researchgate.net/profile/Rui-Oliveira-22'),
    ('orcid', 'https://orcid.org/0000-0003-4114-7570'),
    ('github', 'https://github.com/ruijbo')
)

DEFAULT_PAGINATION = False

# Get the current git commit hash
COMMIT = ''
process = subprocess.Popen('git rev-parse HEAD'.split(), cwd='.',
                           stdout=subprocess.PIPE)
git_hash = process.communicate()[0].strip().decode('utf-8')
if git_hash:
    COMMIT = "{url}/commit/{commit}".format(
    url=SRCURL, commit=git_hash, commit_link=git_hash)

# For modification date in footer
TODAY = datetime.date.today().isoformat()
DEFAULT_DATE = 'fs'

# Theme settings
THEME = 'themes/pure-single'
PROFILE_IMG_URL = 'http://home.uevora.pt/~ruio/static/foto.jpg'
COVER_IMG_URL = 'http://home.uevora.pt/~ruio/static/background.jpg'
TAGLINE = 'Applied Geophysics'
