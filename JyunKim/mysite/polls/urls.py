# URLconf
from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # path(route, view, kwargs, name) - 'app_name:name' 으로 호출
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]