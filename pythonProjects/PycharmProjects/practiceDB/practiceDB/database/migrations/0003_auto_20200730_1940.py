# Generated by Django 3.0.8 on 2020-07-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_database_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='student_roll',
            field=models.IntegerField(),
        ),
    ]
