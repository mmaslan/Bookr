from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=150, help_text='Nazwa wydawnictwa.')
    website = models.URLField(help_text='Witryna wydawnictwa.')
    email = models.EmailField(help_text='Adres email wydawnictwa.')


class Book(models.Model):
    title = models.CharField(max_length=70, help_text='Tutuł książki.')
    publication_date = models.DateField(verbose_name='Data publikacji książki.')
    isbn = models.CharField(max_length=20, verbose_name='Numer ISBN książki.')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')


class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text='Imię lub imiona współtwórców.')
    last_name = models.CharField(max_length=50, help_text='Nazwisko lub nazwiska współtwórców')
    email = models.EmailField(help_text='Email współtwórcy.')


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name='Rola jaką współtwórca odegrał podczas tworzenia tej książki.',
                            choices=ContributionRole.choices, max_length=20)