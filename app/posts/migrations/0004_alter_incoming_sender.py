# Generated by Django 5.1.5 on 2025-01-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_incoming_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming',
            name='sender',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
