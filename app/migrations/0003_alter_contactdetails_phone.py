# Generated by Django 5.0.6 on 2024-08-28 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactdetails",
            name="phone",
            field=models.CharField(max_length=30),
        ),
    ]
