# Generated by Django 3.2.19 on 2023-07-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='OpenHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'open hour',
                'verbose_name_plural': 'open hours',
            },
        ),
    ]
