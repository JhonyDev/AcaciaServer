# Generated by Django 3.2 on 2021-06-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_expression_ver_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='expression',
            name='who_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='expression',
            name='who_profile_image',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
