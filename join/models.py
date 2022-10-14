from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

# Create your models here.
class Member(models.Model) :
    mem_id = models.CharField(primary_key=True, max_length=30)
    mem_name = models.CharField(max_length=50)
    mem_age = models.SmallIntegerField()
    mem_join_date = models.DateTimeField('date published')

    #mem_id.verbose_name = "id"
    #mem_name.verbose_name = "이름"
    #mem_age.verbose_name = "나이"
    #mem_join_date.verbose_name = "가입일"

    @admin.display(
        boolean=True,
        ordering='mem_age',
        description='성인여부'
    )
    def isAdult(self) :
        return self.mem_age >= 20

    def add_ok_string(self) :
        return self.mem_name + "_ok"
    
    def __str__(self) :
        return self.mem_name

class Hobby(models.Model) :
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    hobby_text = models.CharField(max_length=200)

    #hobby_text.verbose_name = "취미"

    def __str__(self) :
        return self.hobby_text    