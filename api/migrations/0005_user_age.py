# Generated by Django 3.2 on 2021-06-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default='18', max_length=50),
        ),
    ]