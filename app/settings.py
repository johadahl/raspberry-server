"""
Settings
"""

from os import getenv

TITLE = "Rasperry Pi Server"

ENVIRONMENT = getenv('APP_ENVIRONMENT')
RELEASE = getenv('GIT_HASH_SHORT', 'NONE')

PORT = int(getenv('PORT', '8080'))
HOST = getenv('HOST')
DEBUG = getenv('DEBUG') == '1'

DATABASE_URL = getenv('DATABASE_URL')
DATABASE_NAME = getenv('DATABASE_NAME')

CRON_ID = getenv('CRON_ID', '1')

# TODO: Replace this with app.core.config instead