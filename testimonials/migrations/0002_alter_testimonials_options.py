# Generated by Django 3.2.19 on 2023-07-06 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonials',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'testimonials'},
        ),
    ]
