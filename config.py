import os
basedir = os.path.abspath(os.path.dirname(__file__))
# base dir = os.path.returns an absolute path (os.path.returns directory name)
class Config(object):
     # DEBUG = True   
     DEBUG = False
     TESTING = False
     QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
     SECRET_KEY = '12345'
    
     UPLOADED_PHOTOS_DEST='app/static/photos'
    
     

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
 
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://charity:21193@localhost/blog"
 
   
class TestingConfig(Config):
    TESTING = True


config_options = {
'test':TestingConfig,
'production':ProductionConfig,
'development': DevelopmentConfig
}
