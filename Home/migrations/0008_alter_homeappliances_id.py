# Generated by Django 5.1.7 on 2025-05-18 10:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Home",
            "0007_rename_appliance_description_homeappliances_description_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="homeappliances",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
