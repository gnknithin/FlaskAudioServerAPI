import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-really-needs-to-be-changed'
    
    MONGODB_SETTINGS = {
        'db':os.environ.get('MONGODB_DB'),
        'host':os.environ.get('MONGODB_HOST') or 'mongodb://localhost/',
        'connect': os.environ.get('MONGODB_CONNECT') or False,
        'port':os.environ.get('MONGODB_PORT') or 27017, 
        'user':os.environ.get('MONGODB_USERNAME'),
        'password':os.environ.get('MONGODB_PASSWORD')
    }

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}