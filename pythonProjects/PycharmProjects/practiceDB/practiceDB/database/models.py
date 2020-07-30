from django.db import models

# Create your models here.

class database(models.Model):
    student_id = models.AutoField
    student_image = models.ImageField(upload_to="database\images", default="")
    student_name = models.TextField()
    student_roll = models.CharField(max_length=50)
    student_class = models.CharField(max_length=50)


    def __str__(self):
        return self.student_name

