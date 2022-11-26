from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False, remin_length=3)
    search_in = forms.CharField(required=False, choices=('title', 'Title', 'contributor', 'Contributor'))