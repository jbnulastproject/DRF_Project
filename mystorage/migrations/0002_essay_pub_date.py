# Generated by Django 2.2.7 on 2019-11-30 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mystorage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]