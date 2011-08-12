#!/usr/bin/env python
# -*- coding:utf-8 -*- 
import os, sys
sys.path.append('/home/p/poncyru/wt/public_html') #каталог с нашими проектами django
sys.path.append('/home/p/poncyru/wt/public_html/wt') #каталог с нашими проектами django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' #указываем на файл /tmp/mysite/setup.py
 
import django.core.handlers.wsgi
 
application = django.core.handlers.wsgi.WSGIHandler()
