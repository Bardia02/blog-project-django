from django import forms
from django.contrib.auth import authenticate
from django.core.validators import ValidationError
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"input100 ","placeholder":"Username"}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"input100","placeholder":"password"}))


    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'),password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError("reiddiiiiii",code="pass wrong")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","email")

