from django.urls import path
from .views import *
urlpatterns = [
    path('' , Students_Details.as_view() , name = 'studentsdetails'),
    path('<int:id>' , Students_Details.as_view()  , name = 'studentdetail')
]
