# Generated by Django 2.2.3 on 2019-08-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_articlebias_reader'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlebias',
            name='used',
            field=models.BooleanField(default=True),
        ),
    ]
