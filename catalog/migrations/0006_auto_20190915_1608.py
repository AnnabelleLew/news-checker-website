# Generated by Django 2.2.5 on 2019-09-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20190829_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(help_text='Enter article text'),
        ),
    ]
