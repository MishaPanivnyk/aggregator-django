from django.contrib import admin

from .models import Blog

# Register your models here.
admin.site.site_header

admin.site.register(Blog)


