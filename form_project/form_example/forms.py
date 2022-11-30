from django import forms
from django.core.exceptions import ValidationError


def validate_email_domain(value):
    if value.split("@")[-1].lower() != "example.com":\
        raise ValidationError("Adres e-mail musi należeć do domeny example.com")


class OrderForm(forms.Form):
    magazine_count = forms.IntegerField(min_value=0, max_value=80, widget=forms.NumberInput(attrs={'placeholder': 'liczba czasopism'}))
    book_count = forms.IntegerField(min_value=0, max_value=50, widget=forms.NumberInput(attrs={'placeholder': 'liczba książek'}))
    send_confirmation = forms.BooleanField(required=False)
    email = forms.EmailField(required=False, validators=[validate_email_domain], widget=forms.EmailInput(attrs={'placeholder': 'Firmowy adres email'}))

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['send_confirmation'] and not cleaned_data.get('email'):
            self.add_error('email', 'Wpisz adres e-mail, aby otrzymać potwierdzenie.')
        elif cleaned_data.get('email') and not cleaned_data['send_confirmation']:
            self.add_error('send_confirmation', 'Zaznacz to pole, jeżeli chcesz otrzymać email z potwierdzeniem.')
        item_total = cleaned_data.get('magazine_count', 0) + cleaned_data.get('book_count', 0)
        if item_total > 100:
            self.add_error(None, 'Całkowita liczba produktów nie może przekroczyć 100.')