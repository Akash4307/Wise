from django import forms

from .models import PdfInfo

class UserForm(forms.ModelForm):

    PdfName = forms.CharField(widget = forms.TextInput(
        attrs={

            'placeholder':'Pdf Book Name',
            'class': 'form-control'

        }
        
    ))

    PdfPrice = forms.CharField(widget = forms.TextInput(
        attrs={

            'placeholder':'Pdf Book Price (Write free if its free)',
            'class': 'form-control'

        }
        
    ))
    
    PdfDescription = forms.CharField(widget = forms.Textarea(
        attrs={

            'placeholder':'Pdf Book Description',
            'class': 'form-control'

        }
        
    ))
    PdfPhoneNumber = forms.CharField(widget = forms.TextInput(
        attrs={

            'placeholder':'Number(optional)',
            'class': 'form-control'

        }
        
    ))
    PdfEmail = forms.CharField(widget = forms.TextInput(
        attrs={

            'placeholder':'Email Address',
            'class': 'form-control'

        }
        
    ))

    class Meta:
        model = PdfInfo
        fields = [

           "PdfName",
           "PdfPrice",
           "PdfBookLogo",
           "PdfFile",
           "PdfDescription",
           "PdfPhoneNumber",
           "PdfEmail",


            
        ]