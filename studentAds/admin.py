from django.contrib import admin
from .models import *

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','owner','category',)
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill',)


class ViewAdmin(admin.ModelAdmin):
    list_display = ('rel_project','session_key_or_user_id', 'date', 'ip')
    ordering = ('rel_project',)

admin.site.register(StudentProject,ProjectAdmin)
admin.site.register(ProjectCategory,CategoryAdmin)
admin.site.register(ProjectView,ViewAdmin)
admin.site.register(RequiredSkill,SkillsAdmin)
