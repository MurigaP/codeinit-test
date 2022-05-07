# Generated by Django 4.0.4 on 2022-05-05 18:54

import api.models.base
import api.models.core.document
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', api.models.base.AutoDateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original_file_name', models.CharField(max_length=500)),
                ('file', models.FileField(upload_to=api.models.core.document.file_upload)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'documents',
            },
        ),
    ]
