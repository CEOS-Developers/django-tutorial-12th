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


### Redirection
# Redirection이란 클라이언트가 서버에 요청 'A'를 보냈는데 서버는 이에 대한 응답으로 'A'가 아닌 'B'를 보내고,
# 서버의 이런 응답을 받은 클라이언트가 'B'로 다시 요청하는 것을 말한다.
## 예를 들어, 학교 게시판에 성적 게시글이 올라왔고, 나는 로그인이 안된 상태로 있다고 하자. 로그인이 안되어있는 걸 모르고 성적 게시글을 클릭하면,
## 나(클라이언트)는 학교(서버)에 성적 게시글을 보여줄 것을 요청하는 것이다.
## 이런 내 요청을 받은 학교(서버)는 내가 로그인 상태가 아니라는 것을 알고, 성적 게시글 대신 로그인 하라고 응답한다.
## 그럼 나(클라이언트)는 학교(서버)의 이런 응답을 받고, 로그인(=다른 요청) 페이지로 이동한다.




### 궁금한 점
# urls.py에서 vote만 int:question_id 부분을 남기고 다른 부분은 pk로 치환했다.
# detail이나 results의 pk대신 question_id를 남겨두고 vote에 pk를 적어둬도 작동하는지 궁금했는데 에러가 발생한다.
# 개인적인 생각으로는 그냥 언어 세팅이 그렇게 되어있는 것 같음