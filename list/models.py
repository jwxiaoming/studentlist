from django.db import models
# Create your models here.

class Grade_Class(models.Model):
    class_text = models.CharField(max_length=200, verbose_name='输入班级')
    student_count = models.IntegerField(default=0,blank=True,null=True, verbose_name='当前人数')
    def __str__(self):
        return self.class_text
    class Meta:
        verbose_name_plural = '班级管理'
        verbose_name = '班级管理'


class Student(models.Model):
    class_text = models.ForeignKey(Grade_Class, on_delete=models.CASCADE, verbose_name='所属班级')
    student_text = models.CharField(max_length=200, verbose_name='学生姓名')
    info_text = models.CharField(max_length=300, default=None, null=True, blank=True, verbose_name='备注信息')
    def __str__(self):
        return str(self.class_text) + ": " +self.student_text
    class Meta:
        verbose_name_plural = '学生名单'
        verbose_name = '学生名单'