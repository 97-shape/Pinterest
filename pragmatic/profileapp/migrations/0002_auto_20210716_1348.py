# Generated by Django 2.2.4 on 2021-07-16 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='massage',
            new_name='message',
        ),
    ]