from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    CATEGORY_CHOICES = [
        ('WATER', 'Water'),
        ('Hostel', 'Hostel'),
        ('Elctricity', 'Elctricity'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=100, default='Unknown')
    contact_number = models.CharField(max_length=15, default='0000000000')
    area = models.CharField(max_length=255, default='Unknown')

    title = models.CharField(max_length=200)
    description = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Other')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.title} - {self.user.username}"
