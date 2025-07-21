from backend.wsgi import 
from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return '¡Hola desde Elastic Beanstalk!'
