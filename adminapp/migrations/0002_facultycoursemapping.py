# Generated by Django 4.2.13 on 2024-07-16 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyCourseMapping',
            fields=[
                ('mappingid', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.faculty')),
            ],
            options={
                'db_table': 'facultycoursemapping_table',
            },
        ),
    ]
