from django import forms

RADIO_CHOICES = (
    ("Wartość pierwsza", "Wyświetlona pierwsza wartość"),
    ("Wartośćc druga", "Wyświetlona druuga wartość"),
    ("Wartość trzecia", "Wyświetlona trzecia wartość")
)

BOOK_CHOICES = (
    (
        "Literatura faktu", (
            ("1", "Deep Learning with Keras"),
            ("2", "Web Development with Django")
        )
    ),
    (
        "Literatura Piękna", (
            ("3", "Brave New World"),
            ("4", "The Great Gatsby")
        )
    )
)


class ExampleForm(forms.Form):
    text_input = forms.CharField(max_length=3)
    password_input = forms.CharField(min_length=8, widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICES)
    books_you_own = forms.MultipleChoiceField(required=False, choices=BOOK_CHOICES)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField(min_value=1, max_value=10)
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField(max_digits=3)
    email_input = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Ukryta wartość")

