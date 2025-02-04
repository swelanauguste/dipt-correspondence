# Generated by Django 5.1.5 on 2025-01-24 12:50

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('received', models.DateTimeField(default=django.utils.timezone.now)),
                ('r_from', models.CharField(max_length=255, verbose_name='received from')),
                ('conf', models.BooleanField(default=False)),
                ('urgent', models.BooleanField(default=False)),
                ('note', models.TextField(blank=True, null=True)),
                ('sender', models.TextField(blank=True, null=True)),
                ('dated', models.DateField()),
                ('subject', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('phone1', models.CharField(blank=True, max_length=15, null=True)),
                ('file', models.FileField(upload_to='incoming/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dated'],
            },
        ),
        migrations.CreateModel(
            name='IncomingComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incoming_comment_created_by', to=settings.AUTH_USER_MODEL)),
                ('incoming', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.incoming')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incoming_comment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Outgoing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('add_to', models.CharField(max_length=255, verbose_name='addressed to')),
                ('conf', models.BooleanField(default=False)),
                ('urgent', models.BooleanField(default=False)),
                ('note', models.TextField(blank=True, null=True)),
                ('dated', models.DateField()),
                ('subject', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='outgoing/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_created_by', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_sender', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dated'],
            },
        ),
        migrations.CreateModel(
            name='OutgoingComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outgoing_comment_created_by', to=settings.AUTH_USER_MODEL)),
                ('outgoing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.outgoing')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outgoing_comment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
