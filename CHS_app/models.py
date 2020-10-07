from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Subjects(models.Model):
    Subject_name = models.CharField(max_length=30)
    Subject_code = models.IntegerField()
    Subject_teacher = models.CharField(max_length=40)


class Teachers(models.Model):
    Tsc_no = models.TextField(max_length=50)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True,default=True)
    phone_number_validator = RegexValidator(regex=r'^(0|\+)\d{8,15}$')
    Phone_Number = models.CharField(validators=[phone_number_validator], max_length=17, unique=True,default=False)


class Parents(models.Model):
    Parents_name = models.CharField(max_length=40)
    Email = models.EmailField(unique=True,max_length=70,default=False)
    phone_number_validator = RegexValidator(regex=r'^(0|\+)\d{8,15}$')
    phone_Number = models.CharField(validators=[phone_number_validator], max_length=17, unique=True)
    Occupation = models.CharField(max_length=50,default=False)



class Student(models.Model):
    Adm_no = models.IntegerField(unique=True)
    First_name = models.CharField(max_length=40)
    Last_name = models.CharField(max_length=40)
    Surname = models.CharField(max_length=40)
    Former_school = models.CharField(max_length=70,default=False)
    KCPE_Marks = models.IntegerField(default=True)
    DateOfBirth = models.DateTimeField(auto_created=True,default=False)
    class_form = models.IntegerField(auto_created=True)
    Subjects_taken = models.IntegerField(Subjects,default=True)
    Admittedon = models.DateTimeField(auto_now_add=True)
    Cleared = models.BooleanField(default=False)

class Fee(models.Model):
    term=models.IntegerField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    IsActive=models.BooleanField(default=True)

class Hostel(models.Model):
    name=models.CharField(max_length=40)
    dormcaptain=models.CharField(max_length=50)
    IsFull=models.BooleanField(default=True)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



