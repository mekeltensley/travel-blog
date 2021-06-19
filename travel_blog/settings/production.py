from travel_blog.settings.common import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['fierce-inlet-31772.herokuapp.com']

# DATABASE CONFIGURATION

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)