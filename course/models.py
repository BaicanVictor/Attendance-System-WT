from django.db import models
from users.models import CustomUser


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, default="")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owner", null=True, blank=True)
    participants = models.ManyToManyField(CustomUser, related_name="participants", null=True, blank=True)


class Attendance(models.Model):
    ATTENDANCE_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )
    attendance_status = models.CharField(max_length=15, choices=ATTENDANCE_CHOICES)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    starting_at = models.DateTimeField()
    ending_at = models.DateTimeField()
    participants = models.ManyToManyField(CustomUser, null=True, blank=True)
    attendances = models.ManyToManyField(Attendance, null=True, blank=True)
