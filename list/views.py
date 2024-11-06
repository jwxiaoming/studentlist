from django.http import HttpResponse
from django.shortcuts import render
from list.models import Student, Grade_Class

# Create your views here.
def index(request):
    students = Student.objects.all()
    grades = Grade_Class.objects.filter(student_count__gt=0)
    # grades = Grade_Class.objects.filter(student_count__gt=0)
    # for student in students:
    #     print(student.id, student.student_text, student.class_text)
    # print('————————分割线————————')
    for i in grades:
        print(students.filter(class_text=i))
    print(grades)
    return render(request, 'index.html', {'students': students, 'grades': grades})