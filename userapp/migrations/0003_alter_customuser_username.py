# Generated by Django 3.2.5 on 2021-09-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='user', max_length=20, unique=True),
        ),
    ]
