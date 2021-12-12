from django.urls import path
from .views import main, teacher_get_classes, view_participants, add_course, add_class, add_attendance, view_attendences

urlpatterns = [
    path('', main, name="main"),
    path('class/<int:course>/', teacher_get_classes),
    path('participants/<int:class_>/', view_participants),
    path('attendences/<int:class_id>/', view_attendences),
    path('add-course/', add_course),
    path('add-class/<int:course>/', add_class),
    path('add-attendance/<int:class_id>/', add_attendance),
]
