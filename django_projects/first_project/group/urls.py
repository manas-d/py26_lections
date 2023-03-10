from django.urls import path

from group.views import students_view, detail_student_view

urlpatterns = [
    path('', students_view),
    path('<int:id>/', detail_student_view)
]

