# Generated by Django 2.1.5 on 2019-05-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0013_auto_20190508_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='complete_view',
            field=models.BooleanField(default=False),
        ),
    ]
