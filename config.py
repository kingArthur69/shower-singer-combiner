import os


class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "download")
    COMBINED_OUTPUT_FOLDER = os.path.join(os.getcwd(), 'combined')


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True


