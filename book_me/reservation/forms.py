import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    password_check = forms.PasswordInput()

    def password_typo_check(self):
        data = self.cleaned_data['password']
        if data != self.cleaned_data['password_check']:
            raise ValidationError("password check is incorrect")
        return data


class ReservationForm(forms.Form):
    title = forms.CharField(required=True)
    start_datetime = forms.DateTimeField(required=True)
    end_datetime = forms.DateTimeField(required=True)
    request_comment = forms.TextInput()
