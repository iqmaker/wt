# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import admin

STATUS_CODES = [
    (1, u'Создан'),
    (2, u'В работе'),
    (3, u'Закрыт'),

]

PRIORITY_CODES = [
    (1, u'Сейчас'),
    (2, u'Быстро'),
    (3, u'Когда-нибудь'),
]

#apps = [app for app in settings.INSTALLED_APPS if not app.startswith('django.')]
AVTOTONUS_RU, PONCY_RU, VSE_RAZBORKI_RU, WT_BUGTRACKER, WT_TODOLIST, WT_QFAQ, WT_SALE, WT_PONCYADMIN = range(1, 9)
PROJECTS = [ 
    ( AVTOTONUS_RU, u'avtotonus.ru'),
    ( PONCY_RU, u'poncy.ru'),
    ( VSE_RAZBORKI_RU, u'vse-razborki.ru'),
    ( WT_BUGTRACKER, u'wt/bugtracker'),
    ( WT_TODOLIST, u'wt/todolist'),
    ( WT_QFAQ, u'wt/qfaq'),
    ( WT_SALE, u'wt/sale'),
    ( WT_PONCYADMIN, u'wt/poncyadmin'),
]
class Ticket(models.Model):
    """Trouble tickets"""
    title = models.CharField(max_length=100, verbose_name=u'Название')
    project = models.IntegerField(blank=True, choices=PROJECTS, verbose_name=u'Проект' )
    submitted_date = models.DateField(auto_now_add=True, verbose_name=u'Дата создания')
    modified_date = models.DateField(auto_now=True, verbose_name=u'Дата изменения')
    submitter = models.ForeignKey(User, related_name="submitter", verbose_name=u'Создал')
    assigned_to = models.ForeignKey(User, verbose_name=u'Принял')
    description = models.TextField(blank=True, verbose_name=u'Описание')
    status = models.IntegerField(default=1, choices=STATUS_CODES, verbose_name=u'Статус')
    priority = models.IntegerField(default=1, choices=PRIORITY_CODES, verbose_name=u'Приоритет')

    def __unicode__(self):
          return self.title

