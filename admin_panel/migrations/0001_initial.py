# Generated by Django 3.2.3 on 2021-07-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminCred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=9)),
            ],
        ),
        migrations.CreateModel(
            name='PaidUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.CharField(max_length=2000)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReportedAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.CharField(max_length=2000)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UnPaidUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.CharField(max_length=2000)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
            ],
        ),
    ]
