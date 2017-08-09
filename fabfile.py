import datetime as dt
from fabric.api import local
import json
import os
import re
import time

# .Env
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def kill_flower():
    """Kill app"""
    local('heroku destroy {0} --confirm {0}'.format(os.environ['HEROKU_FLOWER_NAME']))

def start_flower():
    try:
        kill_flower()
    except:
        print('Probably no flower app running')
    local('heroku create {0}'.format(os.environ['HEROKU_FLOWER_NAME']))
    local('heroku addons:create heroku-postgresql:hobby-dev')
    local('heroku config:set BROKER_URL={}'.format(os.environ['BROKER_URL']))
    # DATABASE_URL set automatically
    local('heroku config:set FLOWER_BASIC_AUTH="{}:{}"'.format(
        os.environ['FLOWER_USER'], os.environ['FLOWER_PASSWORD']))
    local('git push heroku master')
