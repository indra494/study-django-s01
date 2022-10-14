from django.contrib import admin
from .models import Member, Hobby

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['mem_id','mem_name','mem_age']}),
        ('Date information', {'fields': ['mem_join_date'], 'classes':['collapse'] }), 
    ]

admin.site.register(Member,MemberAdmin)
admin.site.register(Hobby)