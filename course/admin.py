from django.contrib import admin
from .models import Course, Class, Attendance

admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Attendance)
