from os import environ
from os.path import realpath, dirname, join

SECRET_KEY = environ.get("SECRET_KEY")
