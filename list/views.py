from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from list.models import Student, Grade_Class
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from.models import Student, CheckedData
import json
from datetime import datetime
# Create your views here.

def check_student_checked_today(request, student_name):
    today = datetime.now().date()
    checked_data = CheckedData.objects.filter(student_name=student_name, check_time__date=today)
    return JsonResponse({'checked': checked_data.exists()})
def get_checkeddata(request):
    try:
        # 获取所有学生数据
        data = CheckedData.objects.all().values()
        data_list = list(data)

        # 根据学生的某个字段（例如'id'或者其他合适的字段）进行倒序排序
        data_list.sort(key=lambda x: x['check_time'], reverse=True)

        return render(request, 'index2.html', {'data': data_list})
    except Exception as e:
        print(e)
        return HttpResponse("获取数据失败")
@csrf_exempt
def record_check(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            check_time = data.get('checkTime')
            #ip_address = data.get('ipAddress')

            student = Student.objects.get(id = student_id)
            CheckedData.objects.create(
                student_name = student.student_text,
                check_time = check_time,
                class_name = student.class_text.class_text,
                #ip_address = ip_address
            )
            return JsonResponse({'message': '记录成功'})
        except Exception as e:
            return JsonResponse({'message': '记录失败，错误原因：{}'.format(str(e))}, status = 500)
    return JsonResponse({'message': '请求方法不允许'}, status = 405)

def index(request):
    students = Student.objects.all()
    grades = Grade_Class.objects.annotate(annotated_student_count=Count('student')).filter(annotated_student_count__gt=0)

    for i in grades:
        print(students.filter(class_text=i))
    print(grades)
    return render(request, 'index3.html', {'students': students, 'grades': grades})


