from typing import Generic
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Member
from django.utils import timezone
from django.views import generic

# Create your views here.
class indexView(generic.ListView):
    template_name = 'join/index.html'
    context_object_name = 'member_list'

    def get_queryset(self) :

        """
        return Member.objects.filter(
            mem_join_date__lte=timezone.now()
        ).order_by('-mem_join_date')[:5]
        """
        return Member.objects.order_by('-mem_join_date')[:5]

class detailView(generic.DetailView) :
    model = Member
    template_name = 'join/detail.html'


class writeView(generic.TemplateView) :
    template_name = 'join/write.html'    

def save(request) :
    try :
        member = Member.objects.create(
            mem_id = request.POST['mem_id']
            , mem_name = request.POST['mem_name']
            , mem_age = request.POST['mem_age']   
            , mem_join_date = timezone.now()      
        )

        for hText in request.POST.getlist('hobby_text') :
            member.hobby_set.create(hobby_text=hText)
    except IntegrityError as e :
        return render(request, 'join/write.html', {
            'member': request.POST,
            'error_message': "이미 존재하는 아이디입니다. 다시 입력해주세요.",
        })
    except Exception as e :
        return render(request, 'join/write.html', {
            'member': request.POST,
            'error_message': "오류가 발생하였습니다.",
        })

    return HttpResponseRedirect(reverse('join:indexView'))