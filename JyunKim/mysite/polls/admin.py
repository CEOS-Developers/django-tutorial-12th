from django.contrib import admin
from .models import Question, Choice
# python manage.py createsuperuser - 관리자 생성

# 관리할 모델 추가
admin.site.register(Question)
admin.site.register(Choice)