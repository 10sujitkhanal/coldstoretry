# Generated by Django 3.2.7 on 2021-11-18 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_movie_movie_rdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shows',
            name='cinema',
        ),
        migrations.DeleteModel(
            name='Cinema',
        ),
    ]