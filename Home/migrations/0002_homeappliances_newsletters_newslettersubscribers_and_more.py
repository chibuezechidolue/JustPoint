# Generated by Django 5.1.7 on 2025-04-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeAppliances",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("appliance_name", models.CharField(max_length=150, unique=True)),
                (
                    "appliance_image",
                    models.FileField(default="default.jpg", upload_to="images/product"),
                ),
                ("appliance_price", models.CharField(max_length=200)),
                ("appliance_description", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="NewsLetters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("subject", models.CharField(max_length=150)),
                ("contents", models.FileField(upload_to="newsletters/")),
            ],
        ),
        migrations.CreateModel(
            name="NewsLetterSubscribers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="UtilityPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "utility_name",
                    models.CharField(default="no advert title", max_length=100),
                ),
                (
                    "utility_image",
                    models.FileField(
                        default="utility-default.jpg", upload_to="images/utility"
                    ),
                ),
                ("payment_url", models.URLField(null=True)),
            ],
        ),
    ]
