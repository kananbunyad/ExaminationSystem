# Generated by Django 3.0.5 on 2023-10-26 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
        ('exam', '0011_auto_20231026_1450'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentAnswers',
            new_name='StudentAnswer',
        ),
    ]