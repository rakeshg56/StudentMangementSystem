# Generated by Django 4.2.13 on 2024-07-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_facultycoursemapping_component_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultycoursemapping',
            name='type',
            field=models.BooleanField(default=True, verbose_name='Faculty Type'),
        ),
    ]