# 1주차 Django tutorial에서 새로 배운 내용들
# 파이썬 언어에 대한 부분보다 Django에 대해 알게된 점 위주로 작성하려 노력
# 했지만 파이썬을 배운 적이 없어서 구분하기 참 어렵디ㅠ

### view 작성 at polls/view.py
# from django.http import HttpResponse
# 클라이언트가 ~/polls 에 대한 Request를 보낼 때 그에 대한 Http Response로 index() 함수를 호출

### Migration
# model 정보 변경에 대한 "가이드문서"
# model 정보 변경 내용을 데이터베이스 구조로 바꿔 보여줄 수 있음
## 관련 명령어
# python manage.py makemigrations <app-name> : Migration 파일 생성
# python manage.py migrate <app-name> : Migration 적용 -> 모델의 변경사항과 DB 내 스키마 동기화
# python manage.py sqlmigrate <app-name> <migration-name> : sql 내역 
## model 변경 적용 순서
# models.py에서 변경 -> makemigrations 명령을 통해 변경사항에 대한 migration 생성 -> migrate를 통해 DB와 동기화

### Model, Class, Field
# Model이란 database의 레이아웃으로, data의 하나의 명확한 요소이다.
# 각 model은 field와 behavior을 가지고 있다. -> 모델은 객체 같은 느낌?
# DB에 데이터를 저장하거나 불러오기 위해 model을 사용한다.
#
# models.py를 작성하면 Django에게 model을 만들었다는 것을 알려줘야 한다 (settings.py에 추가한 polls.apps.PollsConfig' 부분)
# model의 각 field는 Field 인스턴스로 표현된다. polls/models.py 에선 CharField, IntegerField, DateTimeField를 사용했다.
