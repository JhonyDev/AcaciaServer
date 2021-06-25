from django.db import models


# Create your models here.

class AdminCred(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.IntegerField(default=9)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk)
