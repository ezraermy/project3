# Generated by Django 3.2.4 on 2021-07-05 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='date_published',
            new_name='pup_date',
        ),
    ]
