from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, Div

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    choices = forms.CharField(max_length= 30)

    class Meta:
	    model = User
	    fields = ["username","choices","email", "password"]

class LoginForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1")

    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user