# Generated by Django 2.1.7 on 2024-06-26 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0013_auto_20240622_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubjectteacher',
            name='semester',
            field=models.CharField(choices=[('Fourth', 'Fourth'), ('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr'), ('Mr.', 'Mr'), ('Prof Dr.', 'Prof Dr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='upper_degree',
            field=models.CharField(choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Diploma', 'Diploma'), ('PhD', 'PhD')], default='MSc', max_length=30),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(blank=True, choices=[('Fourth', 'Fourth'), ('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr'), ('Mr.', 'Mr'), ('Prof Dr.', 'Prof Dr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms')], max_length=40),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='upper_degree',
            field=models.CharField(choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Diploma', 'Diploma'), ('PhD', 'PhD')], default='MSc', max_length=30),
        ),
    ]
