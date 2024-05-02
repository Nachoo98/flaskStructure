from flask import Flask
from decouple import config
from routes import auth_route,index_route

app = Flask(__name__)

class Config():
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}

configuration = config['development']

app.config.from_object(configuration)

app.register_blueprint(index_route.main, url_prefix='/')
app.register_blueprint(auth_route.main, url_prefix='/auth')


if __name__ == '__main__':
    app.run()
