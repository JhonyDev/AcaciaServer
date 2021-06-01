from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=1000, default='')
    objects = models.Manager()


class Photo(models.Model):
    user_id = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='pictures/%y/%m/%d/', max_length=255, null=False, blank=True)
    objects = models.Manager()


class Interest(models.Model):
    user_id = models.CharField(max_length=100)
    interest = models.CharField(max_length=20)
    objects = models.Manager()
