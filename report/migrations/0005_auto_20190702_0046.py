# Generated by Django 2.2.2 on 2019-07-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20190701_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(),
        ),
    ]
