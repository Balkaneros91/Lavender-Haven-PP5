# Generated by Django 3.2.19 on 2023-07-04 21:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=500, null=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]