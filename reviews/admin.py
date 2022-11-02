from django.contrib import admin

from reviews.models import (
    Publisher,
    Contributor,
    Book,
    BookContributor,
    Review,
)


def isbn13(obj):
    return "{}-{}-{}-{}-{}".format(obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6],
                                   obj.isbn[6:12], obj.isbn[12:13])


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')
    list_filter = ('publisher',)


def initialled_name(obj):
    initials = ''.join([name[0] for name in obj.first_name.split(' ')])
    return "{}, {}".format(obj.last_names, initials)


class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name,)


admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
