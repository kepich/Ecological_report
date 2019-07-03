# Generated by Django 2.2.2 on 2019-07-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20190630_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='mean',
            new_name='ph',
        ),
        migrations.RemoveField(
            model_name='report',
            name='amount_of_probes',
        ),
        migrations.RemoveField(
            model_name='report',
            name='median',
        ),
        migrations.RemoveField(
            model_name='report',
            name='title',
        ),
        migrations.AddField(
            model_name='report',
            name='comment',
            field=models.CharField(default='Information is not found', max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='place',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]
