from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import RegisterUser


# "This is a form that will be used to create a new RegisterUser object."
# 
# The Meta class is used to specify additional information about the form. In this case, we're telling
# Django that the form is associated with the RegisterUser model
class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
        fields = ('full_name', 'email', 'city')
        labels = {
            'full_name': 'Nombre completo',
            'email': 'Correo electronico',
            'city': 'Ciudad'
        }
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                    'placeholder': 'Ingresa tu nombre completo',
                    'autocomplete': 'off'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                    'placeholder': 'Ingresa tu email',
                    'autocomplete': 'off'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': 'autofocus',
                    'placeholder': 'Ingresa tu ciudad',
                    'autocomplete': 'off'
                }
            ),
        }

    def clean_full_name(self):
        """
        The function takes in a string, checks if it's alphabetic, and if it's not, raises a validation
        error
        :return: The full_name
        """
        full_name = self.cleaned_data.get('full_name')
        if full_name.isalpha() == False:
            raise ValidationError(
                "El nombre no puedo contener números ni caracteres especiales"
            )
        if len(full_name) <= 0:
            raise ValidationError(
                "El nombre no puedo ir vacio"
            )
        return full_name

    def clean_email(self):
        """
        If the email is valid, and the email is not already in the database, and the email is not empty,
        then return the email
        :return: The email
        """
        email = self.cleaned_data.get('email')
        if validate_email(email) == False:
            raise ValidationError(
                "Ingrese una dirección de correo electrónico válida."
            )
        if RegisterUser.objects.filter(email=email).first() == True:
            raise ValidationError(
                "Este email ya se encuentra registrado."
            )
        if len(email) <= 0:
            raise ValidationError(
                "El campo email no puede ir vacio"
            )
        return email

    def clean_city(self):
        """
        If the city field contains anything other than letters, raise a validation error. 
        If the city field is empty, raise a validation error. 
        If the city field is valid, return the city. 
        :return: The city
        """
        city = self.cleaned_data.get('city')
        if city.isalpha() == False:
            raise ValidationError(
                "El nombre de la ciudad no puedo contener números ni caracteres especiales"
            )
        if len(city) <= 0:
            raise ValidationError(
                "El campo ciudad no puede ir vacio"
            )
        return city
