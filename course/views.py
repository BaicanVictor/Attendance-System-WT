from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CreateCourseForm, CreateClassForm, CreateAttendanceForm
from .models import Course, Class, Attendance


# get courses
@login_required
def main(request):
    if request.user.is_teacher:
        courses = Course.objects.filter(owner=request.user)
        context = {
            'courses': courses,
        }
        return render(request, "teacher_courses_list.html", context)
    else:
        courses = Course.objects.filter(participants=request.user)
        context = {
            'courses': courses,
        }
        return render(request, "teacher_courses_list.html", context)


@login_required
def teacher_get_classes(request, course):
    course_obj = Course.objects.get(id=course)
    if request.user.is_teacher:
        classes = Class.objects.filter(course=course_obj)
        return render(request, "teacher_classes_list.html", {"classes": classes, "course": course_obj})
    else:
        classes = Class.objects.filter(course=course_obj, participants=request.user)
    return render(request, "teacher_classes_list.html",
                  {"classes": classes.order_by("starting_at"), "course": course_obj})


@login_required
def view_participants(request, class_):
    class_obj = Class.objects.get(id=class_)
    return render(request, "view_participants.html", {"users": class_obj.participants.all()})


@login_required
def view_attendences(request, class_id):
    class_obj = Class.objects.get(id=class_id)
    return render(request, "view_attendences.html", {"attendances": class_obj.attendances.all()})


@login_required
def add_course(request):
    form = CreateCourseForm(request.POST or None)

    if form.is_valid():
        course = form.save(commit=False)
        course.owner = request.user
        course.save()
        form.save_m2m()
        return HttpResponseRedirect(reverse('main'))

    return render(request, "add_course.html", {"form": form})


@login_required
def add_class(request, course):
    form = CreateClassForm(request.POST or None)

    if form.is_valid():
        class_ = form.save(commit=False)
        course_obj = Course.objects.get(id=course)
        class_.course = course_obj
        class_.save()
        form.save_m2m()
        return HttpResponseRedirect(f"/class/{course}")

    return render(request, "add_course.html", {"form": form})


@login_required
def add_attendance(request, class_id):
    class_obj = Class.objects.get(id=class_id)
    if class_obj.attendances.filter(student=request.user).exists():
        return HttpResponseRedirect(f"/class/{class_obj.course.id}")

    form = CreateAttendanceForm(request.POST or None)

    if form.is_valid():
        attendance = form.save(commit=False)
        attendance.student = request.user
        attendance.save()
        class_obj.attendances.add(attendance)
        class_obj.save()
        return HttpResponseRedirect(f"/class/{class_obj.course.id}")

    return render(request, "add_course.html", {"form": form})
