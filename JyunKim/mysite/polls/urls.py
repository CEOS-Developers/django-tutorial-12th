# URLconf
from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # path(route, view, kwargs, name) - {% url 'app_name:name' %}으로 호출
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]