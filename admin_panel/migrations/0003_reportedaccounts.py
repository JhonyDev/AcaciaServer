# Generated by Django 3.2.3 on 2021-06-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_admincred_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportedAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=50)),
            ],
        ),
    ]
