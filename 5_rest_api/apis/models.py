from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 200)
    abbreviation = models.CharField(max_length=50)
    address = models.CharField(max_length = 200)

class Classroom(models.Model):
    grade = models.IntegerField()
    section = models.CharField(max_length = 50)

class Teacher(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 50)

class Student(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 50)
