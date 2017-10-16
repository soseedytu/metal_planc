from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):

    company_uen = forms.CharField(max_length=50)
    company_name = forms.CharField(max_length=50)
    contact_number = forms.CharField(max_length=50)
    tags = forms.MultiValueField(required=False)
    user_name = forms.CharField(max_length=50)
    title = forms.CharField(max_length=50)
    email_address = forms.CharField(max_length=50)
    password = forms.PasswordInput()
    services = forms.TypedMultipleChoiceField(required=False)
    register_as_supplier = forms.CharField()

    #def clean(self):

        # email = self.cleaned_data.get("EmailAddress")
        # upass = self.cleaned_data.get("Password")
        # print("password")
        # print(upass)
        # auth_user = User.objects.filter(username=email)
        # #user = MUser.objects.get(EmailAddress=email)
        # print(auth_user)
        # if auth_user is None:
        #     print("error!")
        #     raise forms.ValidationError("User does not exist!")
        # else:
        #     print('found user!')
        #     return auth_user