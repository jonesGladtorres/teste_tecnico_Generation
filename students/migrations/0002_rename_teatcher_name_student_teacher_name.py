# Generated by Django 4.2.6 on 2023-10-29 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teatcher_name',
            new_name='teacher_name',
        ),
    ]