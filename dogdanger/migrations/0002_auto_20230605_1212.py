# Generated by Django 3.2.4 on 2023-06-05 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogdanger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogdanger',
            name='bites_bolsonaro',
        ),
        migrations.RemoveField(
            model_name='dogdanger',
            name='bites_bush',
        ),
        migrations.RemoveField(
            model_name='dogdanger',
            name='bites_reagan',
        ),
        migrations.RemoveField(
            model_name='dogdanger',
            name='bites_thatcher',
        ),
        migrations.RemoveField(
            model_name='dogdanger',
            name='bites_trump',
        ),
        migrations.RemoveField(
            model_name='dogdanger',
            name='bites_wbush',
        ),
    ]
