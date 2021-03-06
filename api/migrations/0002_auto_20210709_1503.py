# Generated by Django 3.2.3 on 2021-07-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField()),
                ('purpose', models.CharField(default='Subscription', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='paid_fee',
            field=models.BooleanField(default=False),
        ),
    ]
