# Generated by Django 2.2.3 on 2019-08-30 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190829_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(help_text='Enter URL for article', max_length=300),
        ),
    ]
