# -*- coding: utf-8 -*- 
from django.contrib import admin
from wt.sale.models import Manufacture, CarModel, Contact, GoodsGroup, Goods, Presale, PresaleGoods, Sale, SaleGoods, UserPercent
import os


class InlinePresaleGoods(admin.TabularInline):
    model = PresaleGoods
    extra = 1
    
class InlineSaleGoods(admin.TabularInline):
    model = SaleGoods
    extra = 1

class PresaleAdmin( admin.ModelAdmin ):
    list_display = ( 'reg_date', 'contact_name','phone','user',)  
    search_fields = ('contact_name','phone','user', 'description',)    
    list_filter = ('reg_date','user', )
    date_hierarchy = 'reg_date'
    ordering = ('-reg_date', )
    inlines = [InlinePresaleGoods]

class PresaleGoodsAdmin( admin.ModelAdmin ):
    list_display = ( 'presale', 'goods', 'price', 'description' )
    search_fields = ( 'presale', 'goods', 'description' )
    ordering = ( '-id', )
    
class SaleAdmin( admin.ModelAdmin ):
    list_display = ( 'id', 'contact', 'reg_date', 'plan_date', 'fact_date', 'user',)
    search_fields = ('contact','user', 'description',)    
    list_filter = ('reg_date','status', 'user' )
    date_hierarchy = 'reg_date'
    ordering = ('-reg_date',)
    inlines = [InlineSaleGoods]

class SaleGoodsAdmin( admin.ModelAdmin ):
    list_display = ( 'sale', 'goods', 'price', 'bonus', 'count' )
    search_fields = ( 'sale', 'goods', 'description' )
    ordering = ( '-id', )
    
class GoodsAdmin( admin.ModelAdmin ):
    list_display = ( 'car_model', 'group', 'title', 'price', 'color' )
    search_fields = ( 'car_model', 'group', 'title', 'price', 'color' )
    list_filter = ( 'car_model', 'group', 'color' )
    ordering = ( 'car_model', 'group', 'title' )
    
class GoodsGroupAdmin( admin.ModelAdmin ):
    list_display = ( 'main', 'title' )
    search_fields = ( 'title','main' )
    list_filter = ( 'main', )
    ordering = ( 'main', 'title' )
    
class ContactAdmin( admin.ModelAdmin ):
    list_display = ( 'title', 'phone', 'email', 'reg_date',  )
    search_fields = ( 'title','phone', 'email', 'description' )
    list_filter = ( 'title', 'email', 'reg_date' )
    ordering = ( '-reg_date', 'title' )
    
class CarModelAdmin( admin.ModelAdmin ):
    list_display = ( 'manufacture', 'title',  )
    search_fields = ( 'manufacture','title',)
    list_filter = ( 'manufacture', )
    ordering = ( 'manufacture', 'title' )
    
class ManufactureAdmin( admin.ModelAdmin ):
    list_display = ( 'title',)
    ordering = ( 'title', )

class UserPercentAdmin( admin.ModelAdmin ):
    list_display = ( 'user', 'percent' )
    search_fields = ( 'user', 'percent' )
    ordering = ( 'user', 'percent' )
    
admin.site.register(Manufacture, ManufactureAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(GoodsGroup, GoodsGroupAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Presale, PresaleAdmin)
admin.site.register(PresaleGoods, PresaleGoodsAdmin) 
admin.site.register(Sale, SaleAdmin) 
admin.site.register(SaleGoods, SaleGoodsAdmin)
admin.site.register(UserPercent, UserPercentAdmin)
