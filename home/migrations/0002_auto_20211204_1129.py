# Generated by Django 3.2.9 on 2021-12-04 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]