from django.db import models
from django.core.urlresolvers import reverse


class UserInfo(models.Model):
    UserLocation = models.CharField(max_length=500)  
    UserName = models.CharField(max_length=250)
    UserEmail = models.CharField(max_length=1000)
    UserPhoneNumber = models.CharField(max_length=250)
    UserBookName = models.CharField(max_length=1000)
    UserBookPrice = models.CharField(max_length=1000)
    UserBookLogo = models.FileField()
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)


    def get_absolute_url(self):
        return reverse ('sell')

    def __str__(self):
        return self.UserLocation

    
    

    
