# URLconf
from django.urls import path
from . import views  # . = 현재 패키지

urlpatterns = [
    # path(route, view, kwargs, name)
    path('', views.index, name='index'),
]