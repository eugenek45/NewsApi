import os

class Config:
    '''
    General confirguration parent class
    '''

    NEWS_API_BASE_URL="https://newsapi.org/v2/{}?country=us&apiKey={}"

    NEWS_API_KEY='a35f5bd4612a44749d3efbb5c6384f61'


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
