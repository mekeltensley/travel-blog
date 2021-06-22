from travel_blog.settings.settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOST = ['0.0.0.0', 'localhost']

