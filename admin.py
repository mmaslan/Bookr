from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    title_header = 'Aplikacja administracyjna Bookr'
    site_header = 'Aplikacja administracyjna Bookr'
    index_title = 'Administracja witryną Bookr'


class ContributorAdmin(admin.AdminSite):
    list_display = ('last_names', 'first-names')
    list_filter = ('last_names',)
    search_fields = ('last_names_startswith', 'first-names')