# Generated by Django 3.2.7 on 2021-11-18 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20211118_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('farmer', models.AutoField(primary_key=True, serialize=False)),
                ('farmer_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='shows',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='shows',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Shows',
        ),
        migrations.AddField(
            model_name='bookings',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.farmer'),
        ),
    ]