# Generated by Django 2.1.1 on 2019-02-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20190220_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='unit',
            field=models.CharField(choices=[('day', 'day'), ('week', 'week'), ('visit', 'visit')], default='', max_length=30),
        ),
    ]
