from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    EmailAddress = forms.CharField(max_length=100)
    Password = forms.PasswordInput()

    def clean(self):

        email = self.cleaned_data.get("EmailAddress")
        upass = self.cleaned_data.get("Password")
        print("password")
        print(upass)
        auth_user = User.objects.filter(username=email)
        print(auth_user)
        if auth_user is None:
            print("error!")
            raise forms.ValidationError("User does not exist!")
        else:
            print('found user!')
            return auth_user