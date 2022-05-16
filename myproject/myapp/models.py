from django.db import models


# Create your models here.

class Destination(models.Model):
    Dname = models.CharField(max_length=250)
    Dimg = models.ImageField(upload_to='pictures')
    Ddes = models.TextField()

    def __str__(self):
        return self.Dname
