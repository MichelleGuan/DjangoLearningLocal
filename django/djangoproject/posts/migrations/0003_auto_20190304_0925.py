# Generated by Django 2.1.7 on 2019-03-04 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190304_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='bode',
            new_name='body',
        ),
    ]