from travel_blog.settings.common import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOST = ['travel-blog-us.herokuapp.com']
