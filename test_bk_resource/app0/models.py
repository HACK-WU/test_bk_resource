# -*- coding: utf-8 -*-

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table = 'stu'
        verbose_name = '学生'
        verbose_name_plural = '学生'




