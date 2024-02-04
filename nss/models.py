from django.db import models

# Create your models here.
class Department(models.Model):
    dep_id=models.AutoField(primary_key=True)
    dep_name=models.CharField(max_length=20)
class volunteer(models.Model):
    volunteer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    guard_name=models.CharField(max_length=25)
    guard_mob_no=models.IntegerField()
    sex=models.CharField(max_length=15)
    dob=models.DateField()
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
    roll_no=models.IntegerField(unique=False)
    image=models.ImageField(upload_to='volunteers',default="")
    dep_id=models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.name}"
    
class Attendance(models.Model):
    Attendance_id=models.AutoField(primary_key=True)
    vol_id=models.ForeignKey(volunteer,on_delete=models.CASCADE)
    date=models.DateField()
    roll_no=models.IntegerField(null=True)
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=20)
    event=models.CharField(max_length=64)

class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=60)
    date=models.DateField()
    start_time=models.TimeField(auto_now=False, auto_now_add=False)
    end_time=models.TimeField(auto_now=False, auto_now_add=False)
    photo=models.ImageField(upload_to='events')
    des=models.TextField(default="")