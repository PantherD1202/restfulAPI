# Generated by Django 5.1.2 on 2024-10-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("department", models.CharField(max_length=50)),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("hire_date", models.DateField()),
            ],
        options={
                "db_table": "emplyees",
            },
        ),
    ]
