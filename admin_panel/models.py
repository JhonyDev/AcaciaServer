from django.db import models


# Create your models here.

class AdminCred(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.IntegerField(default=9)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk)


class ReportedAccounts(models.Model):
    user_image = models.CharField(max_length=2000)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)

    objects = models.Manager()


class PaidUsers(models.Model):
    user_image = models.CharField(max_length=2000)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)

    objects = models.Manager()


class UnPaidUsers(models.Model):
    user_image = models.CharField(max_length=2000)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)

    objects = models.Manager()


class VerifyUsers(models.Model):
    user_image = models.CharField(max_length=2000)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)

    objects = models.Manager()


class UnVerifyUsers(models.Model):
    user_image = models.CharField(max_length=2000)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)

    objects = models.Manager()
