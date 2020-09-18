from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),#최상위 URLconf에서 polls.urls 모듈을 바라보게 설정한다
    path('admin/', admin.site.urls),
]