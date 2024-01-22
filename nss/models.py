from django.db import models

# Create your models here.
class volunteer(models.Model):
    volunteer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    guard_name=models.CharField(max_length=25)
    guard_mob_no=models.IntegerField()
    sex=models.CharField(max_length=15)
    dob=models.DateField()
    department=models.CharField(max_length=25)
    year=models.IntegerField()
    community=models.CharField(max_length=15)
    address=models.TextField()
    blood_group=models.CharField(max_length=15)
    height=models.IntegerField()
    weight=models.IntegerField()
    mobile_no=models.IntegerField()
    Email_id=models.EmailField()
    year_of_enrollment=models.IntegerField()
    cultural_talents=models.TextField()
    hobbies=models.TextField()
    roll_no=models.IntegerField()
    def __str__(self):
        return f"{self.department}"
class Department(models.Model):
    dep_id=models.AutoField(primary_key=True)
    dep_name=models.CharField(max_length=20)
    roll_no=models.IntegerField(null=True,unique=True)
    name=models.CharField(max_length=30)

class Attendance(models.Model):
    date=models.DateField()
    roll_no=models.IntegerField(null=True)
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=20)
    event=models.CharField(max_length=64)

class Event(models.Model):
    eventname=models.CharField(max_length=60)
    date=models.DateField()