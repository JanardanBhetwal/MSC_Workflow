# Generated by Django 2.1.7 on 2023-08-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_auto_20230813_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubjectteacher',
            name='semester',
            field=models.CharField(choices=[('Second', 'Second'), ('Third', 'Third'), ('First', 'First'), ('Fourth', 'Fourth')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Prof Dr.', 'Prof Dr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms'), ('Mr.', 'Mr'), ('Dr.', 'Dr')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='upper_degree',
            field=models.CharField(choices=[('Diploma', 'Diploma'), ('Masters', 'Masters'), ('PhD', 'PhD'), ('Bachelors', 'Bachelors')], default='MSc', max_length=30),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(blank=True, choices=[('Second', 'Second'), ('Third', 'Third'), ('First', 'First'), ('Fourth', 'Fourth')], max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='aff_type',
            field=models.CharField(choices=[('Permanent', 'Permanent'), ('Visiting', 'Visiting'), ('Contract', 'Contract')], default='Permanent', max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Prof Dr.', 'Prof Dr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms'), ('Mr.', 'Mr'), ('Dr.', 'Dr')], max_length=40),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='upper_degree',
            field=models.CharField(choices=[('Diploma', 'Diploma'), ('Masters', 'Masters'), ('PhD', 'PhD'), ('Bachelors', 'Bachelors')], default='MSc', max_length=30),
        ),
    ]
