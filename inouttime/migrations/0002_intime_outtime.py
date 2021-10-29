# Generated by Django 3.2.8 on 2021-10-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inouttime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=100)),
                ('intime', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=100)),
                ('outtime', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]