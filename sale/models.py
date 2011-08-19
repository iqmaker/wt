# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import os
import settings

class Manufacture( models.Model ):
    title = models.CharField( max_length=64, verbose_name=u'Название' )
    
    def __unicode__(self):
        return self.title
      
    class Meta:
        verbose_name = u"Марка"

class CarModel( models.Model ):
    manufacture = models.ForeignKey( Manufacture, verbose_name=u'Марка' )
    title = models.CharField( max_length=64, verbose_name=u'Название' )
    
    def __unicode__(self):
      return self.title
      
    class Meta:
      verbose_name = u"Модель"

class Contact( models.Model ):
    title = models.CharField( max_length=128, verbose_name=u'Имя' )
    phone = models.CharField( max_length=64, verbose_name=u'Телефон' )
    email = models.EmailField( max_length=36, verbose_name=u'Email', blank=True )
    reg_date = models.DateField( auto_now_add=True, verbose_name=u'Дата регистрации' )
    description = models.TextField( blank=True, verbose_name=u'Описание' )

    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = u"Контактное лицо"


class GoodsGroup( models.Model ):
    title = models.CharField( max_length=36, verbose_name=u'Название' )
    main = models.ForeignKey( 'GoodsGroup', related_name='main_group', verbose_name=u'Вышестоящая группа', blank=True, null=True )
    
    def __unicode__(self):
        return self.title
      
    class Meta:
        verbose_name = u"Группа товаров"

UNDEF_COLOR, WHITE, SILVER, GRAY, YELLOW, ORANGE, BEIGE, GOLD, PINK,RED, VINOUS, BROWN, GREEN, BLUE, BLACK, PURPLE, AQUA, TURQUOISE = [ x for x in range(1, 19) ]
COLOR = (
  ( UNDEF_COLOR, u'Цвет не известен'),
  ( WHITE, u'Белый' ),
  ( SILVER, u'Серебристый' ),
  ( GRAY, u'Серый' ),
  ( YELLOW, u'Желтый' ),
  ( ORANGE, u'Оранжевый' ),
  ( BEIGE, u'Бежевый' ),
  ( GOLD, u'Золотой' ),
  ( PINK, u'Розовый' ),
  ( RED, u'Красный' ),
  ( VINOUS, u'Бордовый' ),
  ( BROWN, u'Коричневый' ),
  ( GREEN, u'Зеленый' ),
  ( BLUE, u'Синий' ),
  ( BLACK, u'Черный' ),
  ( PURPLE, u'Пурпурный' ),
  ( AQUA, u'Голубой' ),
  ( TURQUOISE, u'Бирюзовый' ),
)


class Goods( models.Model ):
    car_model = models.ForeignKey( CarModel, verbose_name=u'Для модели')
    group = models.ForeignKey( GoodsGroup, verbose_name=u'Группа' )
    title = models.CharField( max_length=128, verbose_name=u'Название' )
    price = models.FloatField( verbose_name=u'Цена (руб.)', default=0 )
    color = models.IntegerField( choices=COLOR, verbose_name=u'Цвет детали', default=UNDEF_COLOR )
    
    def __unicode__(self):
        return self.title
      
    class Meta:
        verbose_name = u"Товар"


class Presale( models.Model ):
    reg_date = models.DateField( auto_now_add=True, verbose_name=u'Дата создания' )
    contact_name = models.CharField( max_length=64, verbose_name=u'Имя', default=u'не известно', blank=True )
    phone = models.CharField( max_length=64, verbose_name=u'Телефон')
    description = models.TextField( verbose_name=u'Описание', blank=True )
    user = models.ForeignKey( User, verbose_name=u'Менеджер')

    class Meta:
        verbose_name=u'Запрос';

class PresaleGoods( models.Model ):
    presale = models.ForeignKey( Presale, verbose_name=u'Запрос' )
    goods = models.ForeignKey( Goods, verbose_name=u'Товар')
    price = models.FloatField( verbose_name=u'Цена (руб.)', default=0 )
    description = models.CharField( verbose_name=u'Описание', max_length=128, blank=True )
    
    class Meta:
        verbose_name=u'Товар в запросе';

SALE_PLAN, SALE_FACT, SALE_CANCELED = 1, 2, 3
SALE_STATUS = [ 
    ( SALE_FACT,'Факт'),
    ( SALE_PLAN,'План'),
    ( SALE_CANCELED,'Отмена'),
]
PROFIT_NOTPAYED, PROFIT_PAYED = 1, 2
PROFIT_PAY = [ 
    (PROFIT_NOTPAYED, 'Вознаграждение не выплачено'), 
    (PROFIT_PAYED, 'Вознаграждение выплачено'),
]

class Sale( models.Model ):
    contact = models.ForeignKey( Contact, verbose_name=u'Контактное лицо' )
    reg_date = models.DateField( auto_now_add=True, verbose_name=u'Дата создания' )
    plan_date = models.DateField( verbose_name=u'Плановая дата', blank=True, null=True )
    fact_date = models.DateField( verbose_name=u'Фактическая дата', blank=True, null=True )
    modified_date = models.DateField( auto_now=True, verbose_name=u'Дата изменения' )
    status = models.IntegerField( choices=SALE_STATUS, verbose_name=u'Статус', default=SALE_FACT )
    user_pay = models.IntegerField( choices=PROFIT_PAY, verbose_name=u'Выплата менеджеру', default=PROFIT_NOTPAYED)
    user = models.ForeignKey( User, verbose_name=u'Менеджер')
    description = models.TextField( verbose_name=u'Описание', blank=True )
    
    class Meta:
        verbose_name=u'Продажа';


SALEGOODS_WARRANTY = [ ( x, str( x )) for x in range( 2, 53 ) ] 
SALEGOODS_ONWARRANTY, SALEGOODS_ENDWARRANTY, SALEGOODS_RETURN = 1, 2, 3
SALEGOODS_STATUS = [ 
    (SALEGOODS_ONWARRANTY, 'На гарантии'), 
    (SALEGOODS_ENDWARRANTY, 'Гарантия закончилась'), 
    (SALEGOODS_RETURN, 'Возврат') 
]
    
class SaleGoods( models.Model ):
    sale = models.ForeignKey( Sale, verbose_name=u'Продажа' )
    goods = models.ForeignKey( Goods, verbose_name=u'Товар')
    price = models.FloatField( verbose_name=u'Цена (руб.)', default=0 )
    bonus = models.FloatField( verbose_name=u'Дополнительный бонус менеджеру', default='0' )
    count = models.IntegerField( verbose_name=u'Количество', default='1' )
    warranty = models.IntegerField( choices=SALEGOODS_WARRANTY, verbose_name=u'Гарантия (нед.)', default=2 )
    status = models.IntegerField( choices=SALEGOODS_STATUS, verbose_name=u'Статус', default=SALEGOODS_ONWARRANTY)
    description = models.CharField( verbose_name=u'Описание', max_length=128, blank=True )
    
    class Meta:
        verbose_name=u'Товар в продаже';

class UserPercent( models.Model ):
    user = models.OneToOneField( User, verbose_name=u'Менеджер' )
    percent = models.FloatField( verbose_name=u'Процент', default=5 )

    class Meta:
        verbose_name=u'Процент менеджера';
