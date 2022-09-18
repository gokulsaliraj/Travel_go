from django.db import models

# Create your models here.


class Places(models.Model):
     place_name = models.CharField(max_length=250)
     place_img = models.ImageField(upload_to='pics')
     place_desc = models.TextField()

     def __str__(self):
          return self.place_name

class Member(models.Model):
    member_name = models.CharField(max_length=250)
    member_img = models.ImageField(upload_to='pics')
    member_desc = models.TextField()

    def __str__(self):
        return self.member_name
