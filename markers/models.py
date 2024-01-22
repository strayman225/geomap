from django.db import models




# Create your models here.
class Instituions(models.Model):
    institution = models.CharField(max_length=250)
    category = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    telnumber = models.CharField(max_length=50)
    facebook = models.CharField(max_length=250)

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.institution