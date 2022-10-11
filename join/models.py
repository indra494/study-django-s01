from django.db import models

# Create your models here.
class Member(models.Model) :
    mem_id = models.CharField(primary_key=True, max_length=30)
    mem_name = models.CharField(max_length=50)
    mem_age = models.SmallIntegerField()
    mem_join_date = models.DateTimeField('date published')

    def add_ok_string(self) :
        return self.mem_name + "_ok"
    
    def __str__(self) :
        return self.mem_name

class Hobby(models.Model) :
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    hobby_text = models.CharField(max_length=200)

    def __str__(self) :
        return self.hobby_text    