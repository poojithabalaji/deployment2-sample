# Generated by Django 3.2.4 on 2021-06-06 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poojiapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetails',
            name='address',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='adharnum',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='cgpa',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='mobilenum',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='rank',
        ),
    ]