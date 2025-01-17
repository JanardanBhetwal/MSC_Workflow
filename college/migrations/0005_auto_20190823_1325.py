# Generated by Django 2.1.7 on 2019-08-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_auto_20190818_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubjectteacher',
            name='semester',
            field=models.CharField(choices=[('Third', 'Third'), ('Fourth', 'Fourth'), ('First', 'First'), ('Second', 'Second')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Ms.', 'Ms'), ('Mr.', 'Mr'), ('Dr.', 'Dr'), ('Prof Dr.', 'Prof Dr'), ('Mrs.', 'Mrs')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='upper_degree',
            field=models.CharField(choices=[('Masters', 'Masters'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('PhD', 'PhD')], default='MSc', max_length=30),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(blank=True, choices=[('Third', 'Third'), ('Fourth', 'Fourth'), ('First', 'First'), ('Second', 'Second')], max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='aff_type',
            field=models.CharField(choices=[('Permanent', 'Permanent'), ('Contract', 'Contract'), ('Visiting', 'Visiting')], default='Permanent', max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Ms.', 'Ms'), ('Mr.', 'Mr'), ('Dr.', 'Dr'), ('Prof Dr.', 'Prof Dr'), ('Mrs.', 'Mrs')], max_length=40),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='upper_degree',
            field=models.CharField(choices=[('Masters', 'Masters'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('PhD', 'PhD')], default='MSc', max_length=30),
        ),
    ]
