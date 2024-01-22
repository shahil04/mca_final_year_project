# Generated by Django 4.2.3 on 2023-07-20 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Budget_create_model",
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
                ("budget_name", models.CharField(max_length=100)),
                ("period", models.CharField(max_length=100)),
                ("amount", models.FloatField(max_length=100)),
                ("catagery", models.CharField(max_length=100)),
                ("account", models.CharField(max_length=100)),
                ("label", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Daily_add_model",
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
                    "type_choose",
                    models.CharField(
                        choices=[("income", "INCOME"), ("expense", "EXPENSE")],
                        default="cash",
                        max_length=20,
                    ),
                ),
                ("component", models.CharField(max_length=100)),
                ("amount", models.FloatField(max_length=100)),
                ("date", models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Expanse_add_model",
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
                ("amount", models.FloatField(max_length=100)),
                ("account", models.CharField(max_length=100)),
                ("catagory", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Goal_create_model",
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
                ("goal_name", models.CharField(max_length=100)),
                ("target_amount", models.FloatField(max_length=100)),
                ("saved_already", models.FloatField(max_length=100)),
                ("desired_date", models.DateField()),
                ("notes", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Income_add_model",
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
                ("amount", models.FloatField(max_length=100)),
                ("account", models.CharField(max_length=100)),
                ("catagory", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Transfer_amount_model",
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
                ("amount", models.FloatField(max_length=100)),
                ("from_ac", models.CharField(max_length=100)),
                ("to_ac", models.CharField(max_length=100)),
            ],
        ),
    ]
