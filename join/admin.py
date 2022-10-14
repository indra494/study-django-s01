from django.contrib import admin
from .models import Member, Hobby

# Register your models here.

class HobbyInline(admin.StackedInline):
    model = Hobby
    extra = 2

class MemberAdmin(admin.ModelAdmin):
    list_display = ('mem_id', 'mem_name', 'mem_age', 'isAdult', 'mem_join_date')
    list_filter = ['mem_join_date']
    search_fields = ['mem_name','mem_id']

    fieldsets = [
        (None, {'fields': ['mem_id','mem_name','mem_age']}),
        ('Date information', {'fields': ['mem_join_date'], 'classes':['collapse'] }), 
    ]
    inlines = [HobbyInline]    

admin.site.register(Member,MemberAdmin)
admin.site.register(Hobby)