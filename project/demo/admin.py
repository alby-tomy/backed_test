from django.contrib import admin
from .models import Feedback

# Register your models here.


class demoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'email', 'd_rating', 't_rating')
    search_fields = ('name', 'company_name', 'email') 
admin.site.register(Feedback)