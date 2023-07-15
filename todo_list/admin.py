from django.contrib import admin
from.models import *
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display= ['user','title','creat_at','complete']
    search_fields=['user']
    list_filter=['complete','creat_at']
    
    
admin.site.register(Task,TaskAdmin)