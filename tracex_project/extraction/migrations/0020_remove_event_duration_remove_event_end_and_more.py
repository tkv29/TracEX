# Generated by Django 4.2.11 on 2024-04-30 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extraction', '0019_alter_prompt_category_alter_prompt_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
    ]