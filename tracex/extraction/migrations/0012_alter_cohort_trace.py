# Generated by Django 4.2.7 on 2024-03-19 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("extraction", "0011_alter_cohort_age_alter_cohort_condition_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cohort",
            name="trace",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cohort",
                to="extraction.trace",
            ),
        ),
    ]