from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime
from django import forms

class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name = 'Категория')
    name = models.CharField(max_length=30, verbose_name='Категория транслитом')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __unicode__(self):
        return self.title

class City(models.Model):
    title = models.CharField(max_length=30, verbose_name = 'Город')
    name = models.CharField(max_length=30, verbose_name='Город транслитом')
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    def __unicode__(self):
        return self.title

class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'Заголовок')
    description = models.TextField(verbose_name = 'Описание')
    timestamp = models.DateTimeField(default=datetime.now())
    price = models.IntegerField(verbose_name = 'Цена')
    category = models.ForeignKey(Category, verbose_name = 'Категория')
    city = models.ForeignKey(City, verbose_name = 'Город')
    user = models.ForeignKey(User)
    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

class AdForm(ModelForm):
    class Meta:
        model = Ad
        exclude = ('timestamp', 'user')

admin.site.register(Ad, AdAdmin)
admin.site.register(Category)
admin.site.register(City)