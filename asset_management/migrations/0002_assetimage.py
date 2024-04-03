# Generated by Django 5.0.2 on 2024-02-27 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='asset_images/')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='asset_management.asset')),
            ],
        ),
    ]
