# Generated by Django 2.1.7 on 2024-07-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0014_auto_20240626_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubjectteacher',
            name='semester',
            field=models.CharField(choices=[('Second', 'Second'), ('First', 'First'), ('Third', 'Third'), ('Fourth', 'Fourth')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Prof Dr.', 'Prof Dr'), ('Dr.', 'Dr'), ('Ms.', 'Ms')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='upper_degree',
            field=models.CharField(choices=[('Diploma', 'Diploma'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PhD', 'PhD')], default='MSc', max_length=30),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(blank=True, choices=[('Second', 'Second'), ('First', 'First'), ('Third', 'Third'), ('Fourth', 'Fourth')], max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='aff_type',
            field=models.CharField(choices=[('Contract', 'Contract'), ('Visiting', 'Visiting'), ('Permanent', 'Permanent')], default='Permanent', max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Prof Dr.', 'Prof Dr'), ('Dr.', 'Dr'), ('Ms.', 'Ms')], max_length=40),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='upper_degree',
            field=models.CharField(choices=[('Diploma', 'Diploma'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PhD', 'PhD')], default='MSc', max_length=30),
        ),
    ]