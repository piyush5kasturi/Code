# Generated by Django 3.0.8 on 2020-07-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20200730_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='student_roll',
            field=models.CharField(max_length=50),
        ),
    ]
