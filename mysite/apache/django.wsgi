import os
import sys
path = '/var/www/'
if path not in sys.path:
    sys.path.insert(0, path + "mysite") 
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
