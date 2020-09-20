안녕하세요 README 부분을 작성하지 않아 다시 보내게 되었습니다!

백엔드 개발은 처음이라 여러가지로 신기한 경험이었던 것 같습니다
사실 아직 장고가 어떤 원리로 동작하는건지 잘 모르겠지만 앞으로 있을 스터디에서 많이 배울 수 있을 것 같아 기대가 됩니다
감사합니다

1. views.py

- Django에서의 뷰(View)는 다른 일반 MVC Framework에서 말하는 Controller와 비슷한 역할 을 한다.
즉, View는 필요한 데이터를 모델(model)에서 가져와서 적절히 가공하여 웹페이지 결과를 만들도록 컨트롤하는 역할을 한다.
(ex. Views.py에서 Front-End 에서 오는 HTTP Request를 입력 parameter로 받아들이고, HTTP Response를 return해주는 View를 만들수있다.)

! 각 함수가 하나의 View를 정의한다
! 각 View는 HTTP Request를 입력 파라미터로 받아들이고 HTTP Response를 리턴한다
! Http404 같은 Exception을 리턴하기도 함 -> shortcut가능

ex. from django.http import HttpResponse
    def index(request):
        return HttpResponse("<h1>Hello, World!</h1>")

2. urls.py 

- Django내에서 Web service를 제공하는데 url를 넘기기 전에 main페이지와 각 app들과 url를 mapping해주는 기능을 django ulrs.py에서 지원한다
- app들이 다양해지고 app하위에 또다른 기능들이 생기면 main urls.py에서 모든 url를 mapping하지 않고 하위 app urls.py에 각 기능에 대한 url를 위탁할 수 있다.

3. runserver
- Server를 실행하여 http request를 요청하고 요청한 값을 response 받아본다
- runserver는 manage.py가 있는 디렉토리에서 실행한다

4. Migration
- Django에서 Model 클래스를 생성하고 난 후, 해당 모델에 상응하는 테이블을 데이터베이스에서 생성할 수 있다
- Python 모델 클래스의 수정을 DB에 적용하는 과정을 Migration이라 부른다

방법
- settings.py 파일 안의 INSTALLED_APPS 리스트에 Django App을 추가한다
- ./manage.py makemigrations 수행한다
-> Django App안에 migrations라는 서브 폴더를 만들고 테이블 생성 및 수정을 위한 파이썬 마이그레이션 파일을 생성한다

5. Django Template
- Django에서는 공통적으로 들어가는 HTML 코드를 기본 템플릿으로 만들고, 각 웹페이지마다 변경이 필요한 부분만 코드를 작성하게 하는 템플릿 확장 기능을 제공한다
- Base Directory 밑에 templates라는 서브 폴더 만들어 html 작성

6. models.py
- Django에서 모델은 데이터 서비스를 제공하는 layer이다.
- 하나의 모델 클래스는 데이터베이스에서 하나의 테이블에 해당한다.

** 실행 시 떴던 오류
- Runserver 에러..
- github 에러..