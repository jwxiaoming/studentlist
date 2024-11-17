from django.urls import path
from . import views
from.views import record_check,get_checkeddata,check_student_checked_today

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('record_check', record_check, name='record_check'),
    path('get_checkeddata', get_checkeddata, name='get_checkeddata'),
    path('check_student_checked_today/<str:student_name>/', check_student_checked_today),
]