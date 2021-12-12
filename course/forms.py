from django import forms
from django.forms import DateTimeInput, SelectMultiple, Select

from .models import Course, Class, Attendance


class CreateCourseForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=100, label="Description",
                                  widget=forms.Textarea(attrs={'class': 'form-control'}))
    participants = forms.SelectMultiple(attrs={'class': 'form-control'})

    class Meta:
        model = Course
        fields = '__all__'
        exclude = ('owner',)


class CreateClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['starting_at', 'ending_at', 'participants']
        widgets = {
            'starting_at': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'ending_at': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'participants': SelectMultiple(attrs={'class': 'form-control'}),
        }


class CreateAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['attendance_status']
        widgets = {
            'attendance_status': Select(attrs={'class': 'form-control'}),
        }
