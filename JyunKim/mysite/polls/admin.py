from django.contrib import admin
from .models import Question, Choice


# 관리할 모델 추가
admin.site.register(Question)
admin.site.register(Choice)