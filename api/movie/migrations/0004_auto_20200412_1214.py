# Generated by Django 3.0.4 on 2020-04-12 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200412_1120'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together=set(),
        ),
    ]
