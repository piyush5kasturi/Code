# Generated by Django 3.0.8 on 2020-07-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='student_roll',
            field=models.CharField(default='', max_length=50),
        ),
    ]