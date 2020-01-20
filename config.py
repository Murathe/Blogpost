import os

class Config:
    '''
    General - parent configuration class
    '''
    QUOTE_API_KEY_BASE = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('secret_key')
    UPLOADEDE_PHOTO_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<enterpd>:<enterpd>@localhost/<enterbf>'


class ProdConfig(Config):
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = '+test'

class   DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = True

config_option = {
    'development': DevConfig,
    'production': ProdConfig,
    'text': TestConfig
}


