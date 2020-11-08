from django.db import models


class plasmaregister(models.Model):
     first_name = models.CharField(max_length=30)
     mob_number = models.IntegerField()
     email_id= models.CharField(max_length=30)
     blood_group=models.CharField(max_length=30)
     recovered_date= models.DateField()

     def __str__(self):
        return self.first_name
