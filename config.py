from os import environ

MAIL_USERNAME=environ.get('MAIL_USERNAME')
MAIL_PASSWORD=environ.get('MAIL_PASSWORD')
MAIL_PORT=environ.get('MAIL_PORT')
MAIL_DEFAULT_SENDER=environ.get('MAIL_DEFAULT_SENDER')
MAIL_TO=environ.get('MAIL_TO')
MAIL_SERVER=environ.get('MAIL_SERVER')