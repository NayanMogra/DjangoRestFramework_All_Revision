from django.urls import path
from .views import *
urlpatterns = [
    path('' , students_details , name = 'studentsdetails'),
    path('<int:id>' , student_detail , name = 'studentdetail')
]
