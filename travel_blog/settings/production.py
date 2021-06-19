from travel_blog.settings.common import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'fierce-inlet-31772.herokuapp.com']
