from django.contrib import admin
from django.contrib.auth.admin import User


class BookrAdmin(admin.AdminSite):
    site_header = "Administracja witryną Bookr"


admin_site = BookrAdmin(name='bookr_admin')
admin_site.register(User)

# Register your models here.
