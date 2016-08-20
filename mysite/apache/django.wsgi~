import os
import sys
path = '/var/www/mysite'
if path not in sys.path:
sys.path.insert(0, '/var/www/mysite/') #将网站工程目录临时加入ubuntu系统环境中
os.environ['DJANGO_SETTINGS_MODULE'] = ' mysite.settings'
 #新建一个环境变量DJANGO_SETTINGS_MODULE，目的是指向网站工程的settings.py
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
