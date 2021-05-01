from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import User, ReferCode


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    used_refer_code = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "referrer_code",
                "class": "form-control"
            }
        ))

    def clean_used_refer_code(self):
        code = self.cleaned_data.get('used_refer_code')

        if code:
            try:
                referrer_codeObj = ReferCode.objects.get(code=code)
                return referrer_codeObj
            except ReferCode.DoesNotExist:
                raise ValidationError("code is invalid, if you don't have valid code leave blank'")

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'used_refer_code')
