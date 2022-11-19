from django import forms

RADIO_CHOICE = (('Wartość pierwsza', 'Wyświetlona pierwsza wartość', 'Wartość druuga', 'Wyświetlona druga wartość',
                 'Wartość trzecia', 'Wyświetlona trzecia wartość'))

BOOK_CHOICE = (('Literatura faktu',
                (('1', 'Deep Learning with Keras',
                  '2', 'Web Development with Django'))),
               ('Literatura piękna',
                (('3', 'Brave New World'),
                 '4', 'The Great Gatsby')))


class ExampleForm(forms.Form):
    text_input = forms.CharField()
    password_input = forms.CharField(widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICE, widget=forms.RadioSelect)
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICE)
    books_you_own = forms.MultipleChoiceField(choices=BOOK_CHOICE)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField()
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField()
    email_input = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={'type': 'data'}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial='Ukryta wartosc')
