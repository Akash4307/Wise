from django.db import models
from django.urls import reverse


class PdfInfo(models.Model):
    PdfName = models.CharField(max_length=500) 
    PdfPrice = models.CharField(max_length=6, null=False, blank=False)
    PdfDescription = models.CharField(max_length = 10000, null=False)

    PdfPhoneNumber = models.CharField(max_length = 10000, null=True, blank=True)

    PdfEmail = models.CharField(max_length = 10000, null=False)

    PdfBookLogo = models.FileField(max_length=10000) 
    PdfFile = models.FileField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def get_absolute_url(self):
        return reverse ('sell')

    def __str__(self):
        return self.PdfName



    
    
    

    
