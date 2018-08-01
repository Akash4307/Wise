from django import forms

from .models import UserInfo

class UserForm(forms.ModelForm):

    Discription = forms.CharField( widget=forms.Textarea (


        attrs={
            'placeholder':'Description',
            'class': 'form-control',
        }
    ))
    UserBookName = forms.CharField( widget=forms.TextInput (


        attrs={
            'placeholder':'Book Name',
            'class': 'form-control',
                    
                    


        }
    ))
    UserBookPrice = forms.CharField( widget=forms.TextInput (


        attrs={
            'placeholder':'Book Price',
            'class': 'form-control'

        }
    ))
    UserName = forms.CharField( widget=forms.TextInput (


        attrs={
            'placeholder':'Name',
            'class': 'form-control'

        }
    ))
    UserPhoneNumber = forms.CharField( widget=forms.TextInput (


        attrs={
            'placeholder':'Number(optional)',
            'class': 'form-control'

        }
    ))
    UserEmail = forms.CharField( widget=forms.TextInput (


        attrs={
            'placeholder':'Email address',
            'class': 'form-control'

        }
    ))
    UserLocation = forms.CharField( widget=forms.TextInput (


        attrs={
            'placeholder':'Your City Name',
            'class': 'form-control'

        }
    ))


    class Meta:
        model = UserInfo
        fields = (
            "UserBookName",
            "Discription",
            "UserName",

            "UserLocation",
            "UserEmail",
            "UserPhoneNumber",
            "UserBookPrice",
            "UserBookLogo",

            
        )


