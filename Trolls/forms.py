from django import forms

from .models import UserInfo

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [

            "UserLocation",
            "UserName",
            "UserBookName",
            "UserEmail",
            "UserPhoneNumber",
            "UserBookPrice",
            "UserBookLogo",

            
        ]

        labels = {
            'UserLocation': ('Location'),
            'UserName': ('Name'),
            'UserBookName': ('Book Name'),
            'UserEmail': ('Email'),
            'UserPhoneNumber': ('PhoneNumber'),
            'UserBookPrice': ('Book Price'),
            'UserBookLogo': ('Book Image'),        }