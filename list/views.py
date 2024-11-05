from django.http import HttpResponse
from django.shortcuts import render
from list.models import Student, Grade_Class

# Create your views here.
def index(request):
    students = Student.objects.all()
    grades = Grade_Class.objects.all()
    for student in students:
        print(student.id, student.student_text, student.class_text)
    print('————————分割线————————')

    return render(request, 'index.html', {'students': students, 'grades': grades})