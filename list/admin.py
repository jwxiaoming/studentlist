from django.contrib import admin
from list.models import Grade_Class, Student

class GradeClassAdmin(admin.ModelAdmin):
    list_display = ('class_text',)
    fields = ('class_text',)


admin.site.register(Grade_Class, GradeClassAdmin)
admin.site.register(Student)