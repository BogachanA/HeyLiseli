from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Liseli


from .models import Provider, Internship, IntCategory

# Register your models here.


class IntAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'provider', 'date_published',)
    ordering = ('-date_published',)


class IntCatAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('company_name',)


admin.site.register(Liseli, UserAdmin)
admin.site.register(Internship, IntAdmin)
admin.site.register(IntCategory, IntCatAdmin)
admin.site.register(Provider,ProviderAdmin)

