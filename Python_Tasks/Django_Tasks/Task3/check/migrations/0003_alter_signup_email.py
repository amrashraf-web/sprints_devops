# Generated by Django 4.2.1 on 2023-05-16 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_alter_signup_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='Email',
            field=models.CharField(max_length=200),
        ),
    ]
