from travel_blog.settings.common import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOST = ['0.0.0.0', 'localhost']
