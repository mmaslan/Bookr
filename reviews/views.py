from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PublisherForm, SearchForm, ReviewForm
from .models import Book, Contributor, Publisher, Review
from .utils import average_rating


def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = Contributor.objects.filter(first_names__iscontain=search)
            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

            lname_contributors = Contributor.objects.filter(last_names__iscontain=search)
            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

    return render(request, "reviews/search-results.html", {'form': form, 'search_text': search_text, 'books': books})


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})

    context = {
        'book_list': book_list
    }
    return render(request, 'reviews/book_list.html', context)


def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
    else:
        review = None

    if request.method == 'Post':
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            update_review = form.save(False)
            update_review.book = book

            if review is None:
                messages.success(request)


def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None
        if request.method == 'Post':
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, 'Obiekt Publisher \"{}"\ został utworzony.'.format(updated_publisher))
            else:
                messages.success(request, 'Obiekt Publisher \"{}"\ został uaktywniony.'.format(updated_publisher))
            return redirect('publisher_edit', updated_publisher.pk)
        else:
            form = PublisherForm(instance=publisher)

    return render(request, 'form-example.html', {'method': request.method, 'form': form})