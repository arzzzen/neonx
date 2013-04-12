from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.admin import UserAdmin

class Profile(models.Model):
    user = models.OneToOneField(User)
    # Здесь поля из других приложений
    city = models.ForeignKey("ad.City", verbose_name = 'Город')
    # -------------------------------
    def __unicode__(self):
        return self.user.username
        
class UserCreateForm(ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    class Meta:
        model = Profile
        fields = ("city",)
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        usercreate = User.objects.create_user(username = self.cleaned_data['username'], password = self.cleaned_data['password'])
        Profile.objects.create(user = usercreate, city = self.cleaned_data['city'])
        return user

class ProfileInline(admin.StackedInline):
    model = Profile

class ProfileAdmin(UserAdmin):
    inlines = [ ProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)