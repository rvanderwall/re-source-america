'''
Created on Aug 26, 2012

@author: robertv
'''
from rSrcApp.models import Project, ProjectSkill
from django.contrib import admin


class ProjectSkillInline(admin.TabularInline):
    model = ProjectSkill
    extra = 2
    
class ProjectAdmin(admin.ModelAdmin):
    fields = ['post_date', 'title', 'due_date', 'license']
    inlines = [ProjectSkillInline]
    list_display=('title', 'description', 'price', 'is_new')
    
admin.site.register(Project, ProjectAdmin)
