# Generated by Django 3.2 on 2021-06-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_photo_is_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_status',
            field=models.CharField(default='Unverified', max_length=20),
        ),
    ]
