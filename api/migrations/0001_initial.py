# Generated by Django 3.2.3 on 2021-07-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_name', models.CharField(default='', max_length=50)),
                ('who_profile_image', models.CharField(default='', max_length=1000)),
                ('who_liked', models.CharField(max_length=100)),
                ('who_work', models.CharField(default='', max_length=100)),
                ('whom_liked', models.CharField(max_length=100)),
                ('exp', models.CharField(default='None', max_length=50)),
                ('whom_name', models.CharField(default='', max_length=50)),
                ('whom_work', models.CharField(default='', max_length=50)),
                ('profile_image', models.CharField(default='', max_length=1000)),
                ('ver_status', models.CharField(default='Unverified', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('interest', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('is_id', models.CharField(default='false', max_length=10)),
                ('picture', models.ImageField(blank=True, max_length=255, upload_to='pictures/%y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_email', models.CharField(default='not_avail', max_length=100)),
                ('age', models.CharField(default='18', max_length=50)),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=100)),
                ('verification_status', models.CharField(default='Unverified', max_length=20)),
                ('about', models.CharField(max_length=100)),
                ('interest', models.CharField(max_length=100)),
                ('work', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('profile_image', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
