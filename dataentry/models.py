from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=250)
    roll_no = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.name