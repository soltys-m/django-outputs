# Generated by Django 2.1.7 on 2019-04-04 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outputs', '0012_set_export_query_string'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='export',
            name='params',
        ),
    ]
