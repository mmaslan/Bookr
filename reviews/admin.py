from django.contrib.admin import AdminSite

from reviews.models import (
    Publisher,
    Contributor,
    Book,
    BookContributor,
    Review
)


class BookrAdminSite(AdminSite):
    title_header = 'Aplikacja administracyjna Bookr'
    site_header = 'Aplikacja administracyjna Bookr'
    index_title = 'Administracja witryną Bookr'


admin_site = BookrAdminSite


admin_site.register(Publisher)
admin_site.register(Contributor)
admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Review)