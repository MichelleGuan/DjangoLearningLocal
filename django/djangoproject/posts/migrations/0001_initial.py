# Generated by Django 2.1.7 on 2019-03-01 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('bode', models.TextField()),
                ('create_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
