# Generated by Django 3.0.4 on 2020-03-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='username',
            field=models.CharField(default='default', max_length=255),
        ),
    ]
