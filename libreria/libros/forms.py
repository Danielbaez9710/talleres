from django import forms
from .models import Author, Book

#Crear formulario
class AuthorForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Author

        #especificar los campos
        fields = [
            'first_name',
            'last_name',
            'photo',
            'birth_date'
        ]

# creating a form
class Libros(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Book
 
        # specify fields to be used
        fields = [
            "id",
            "name",
            "description",
            "year",
            "cost",
            "author",
        ] 