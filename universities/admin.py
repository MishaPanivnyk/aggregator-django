from django.contrib import admin

from universities.models import University, TopUniversity

# Register your models here.

admin.site.register(University)
admin.site.register(TopUniversity)