from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import *

# Register your models here.


class LiseliUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Liseli


class LiseliAdmin(UserAdmin):
    form = LiseliUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('lise', 'grade','gender','user_image')}),
    )


class LiseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class IntAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'provider', 'date_published', 'view_count')
    ordering = ('-date_published',)


class VolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'provider', 'date_published', 'view_count')
    ordering = ('date_published',)


class IntCatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class VolCatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('company_name',)


class IntViewAdmin(admin.ModelAdmin):
    list_display = ('rel_int', 'session_key_or_user_id', 'date', 'ip')
    ordering = ('rel_int',)


class VolViewAdmin(admin.ModelAdmin):
    list_display = ('rel_vol', 'session_key_or_user_id', 'date', 'ip')
    ordering = ('rel_vol',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session')
    ordering = ('user',)


admin.site.register(Liseli, LiseliAdmin)
admin.site.register(Lise, LiseAdmin)
admin.site.register(Internship, IntAdmin)
admin.site.register(VolunteerProject,VolAdmin)
admin.site.register(IntCategory, IntCatAdmin)
admin.site.register(VolCategory,VolCatAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Provider,ProviderAdmin)
admin.site.register(Int_View, IntViewAdmin)
admin.site.register(VolView, VolViewAdmin)
admin.site.register(LiseliSession, SessionAdmin)

