# Generated by Django 3.0.5 on 2023-10-26 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
        ('exam', '0010_auto_20231026_1448'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentAnswer',
            new_name='StudentAnswers',
        ),
    ]
