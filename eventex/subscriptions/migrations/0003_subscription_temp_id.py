# Generated by Django 3.2.12 on 2022-05-11 00:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20220505_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='temp_id',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
