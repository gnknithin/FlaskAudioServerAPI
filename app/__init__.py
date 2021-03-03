import sys
try:
    from flask import Flask
    from flask_mongoengine import MongoEngine
    from config import config
    import wtforms_json
except ModuleNotFoundError:
    print("\nFlask, Flask-Mongoengine, WTForms, WTForms-JSON must be Installed\n")
    sys.exit(0)


mongodb = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    config[config_name].init_app(app)

    wtforms_json.init()
    
    mongodb.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app