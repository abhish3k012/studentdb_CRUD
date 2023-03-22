from django.db import models

class student(models.Model):
    s_name=models.CharField(max_length=50)
    s_age=models.IntegerField()
    s_mobile=models.CharField(max_length=50)
    s_address=models.CharField(max_length=50)
    s_marks=models.IntegerField()