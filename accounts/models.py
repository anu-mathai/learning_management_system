from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):

    ROLE_CHOICES = [
       ('STUDENT','student'),
       ('FACULTY','faculty'),
    ]

    phone = models.CharField(max_length=15,unique= True)

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='STUDENT')

class TrainerProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='trainer_profile')

    qualification = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    experience = models.PositiveIntegerField(default=0)

class StudentProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')

    address = models.TextField(null=True, blank=True)

    age = models.PositiveIntegerField()

    enrollment_number = models.CharField(max_length=20, unique=True)
    