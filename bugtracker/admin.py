# -*- coding:utf-8 -*-
from django.contrib import admin
from wt.bugtracker.models import Ticket

class TicketAdmin( admin.ModelAdmin  ):
    list_display = ('title', 'project', 'status', 'priority', 'submitter', 'submitted_date', 'modified_date')
    list_filter = ('priority', 'status', 'project', 'submitted_date')
    search_fields = ('title', 'description',)    
    ordering = ('status', 'priority', 'submitted_date', 'title')

admin.site.register( Ticket, TicketAdmin )
