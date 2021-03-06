import os

class Config:
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Amin1234@localhost/blogs'


    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    #SQLALCHEMY_DATABASE_URI = "postgresql://mqtrcwkoyajdls:d9140b4145e49978aab6a5642c8ab79074c41af39a5955a362108b1777ba5e05@ec2-52-21-252-142.compute-1.amazonaws.com:5432/dfdj7mklrqk41n?sslmode=require"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SECRET_KEY=os.environ.get("SECRET_KEY")
class DevConfig(Config):
    
    DEBUG = True
    ENV = 'development'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Amin1234@localhost/blogs'



config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}