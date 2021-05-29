from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    objects = models.Manager()


class Photo(models.Model):
    photo_id = models.CharField(max_length=5000, primary_key=True, default="")
    user_id = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='pictures/%y/%m/%d/', max_length=255, null=False, blank=True)
    objects = models.Manager()
