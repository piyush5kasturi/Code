from django.db import models

# Create your models here.

class database(models.Model):
    student_id = models.AutoField
    student_image = models.ImageField

