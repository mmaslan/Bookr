from django import forms
from .forms import SearchForm


class SearchForm(forms.Form):
    search = forms.CharField(min_length=3)
    search_in = forms.CharField()