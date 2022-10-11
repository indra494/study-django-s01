from django.urls import path
from . import views

app_name = 'join'
urlpatterns = [
    path('', views.indexView.as_view(), name='indexView'),
    path('detail/<str:pk>/', views.detailView.as_view(), name='detailView'),
    path('write/', views.writeView.as_view(), name='writeView'),
    path('write/save', views.save, name='save')
]