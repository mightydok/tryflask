CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Stackexchange', 'url': 'https://openid.stackexchange.com/' },
    { 'name': 'Steam', 'url': 'https://steamcommunity.com/openid/' }
]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# mail server settings
# python -m smtpd -n -c DebuggingServer localhost:25
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['vitaliy.okulov@gmail.com']

# pagination
POSTS_PER_PAGE = 3
