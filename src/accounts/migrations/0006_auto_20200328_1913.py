# Generated by Django 3.0 on 2020-03-28 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200328_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='tags',
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
