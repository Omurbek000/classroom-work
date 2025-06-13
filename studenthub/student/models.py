from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}: {self.email}"
