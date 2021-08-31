""" Setting Up the App Configuration"""
import os

class Config: 
    SECRET_KEY = os.environ.get("SECRET_KEY", "cancookliam0671123456") or os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    """ Configuration for Development Environment. """
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE') or 'postgresql:///recipe'

class TestingConfig(Config):
    """Configurations for Testing Environment."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE') or 'postgresql:///recipe_test'

class ProductionConfig(Config):
    """Configurations for Production Environment."""
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app_config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
};