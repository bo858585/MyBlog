# Django settings for blog app for tests.

import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': "/".join([PROJECT_PATH, "db.sqlite"]),
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*892=_ptyr_%am49t#tp#&bk8nnag!*h4nrpi7xb+m7b)5(!$#'

ROOT_URLCONF = 'blog.urls'

INSTALLED_APPS = (
    'blog',
)
