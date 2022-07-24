# -*- coding: utf-8 -*-
from src.main import app

def create_app_for_gunicorn():
    app.config['DEBUG'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app

# If you want to run in your console, please use 
# gunicorn -c config/gunicorn_config.py  "prod:create_app_for_gunicorn()"