# Generated by Django 3.2.19 on 2023-07-04 20:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=500, null=True)),
                ('message_subject', models.CharField(max_length=50, null=True, verbose_name='subject')),
                ('message', models.TextField(max_length=1000, null=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
