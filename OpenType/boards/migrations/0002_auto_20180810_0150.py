# Generated by Django 2.0.7 on 2018-08-09 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='last_added',
            new_name='last_updated',
        ),
    ]
