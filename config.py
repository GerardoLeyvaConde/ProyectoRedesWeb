import os

class Config(object):
    SECRET_KEY= 'my_secrete_key'

class DevelopmentConfig(Config):
    DEBUG= True