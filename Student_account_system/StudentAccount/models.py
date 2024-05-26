from django.db import models

# Create your models here.
class StudentData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    birthday = models.DateField()
    email = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=11)
    year = models.PositiveIntegerField()
    course = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"