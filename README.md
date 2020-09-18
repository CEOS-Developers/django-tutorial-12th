# django-tutorial-12th

[스터디 내용](https://www.notion.so/1-Django-tutorial-43bd49334db6449c96d9b336b31cf2ac)  

[본인 github 아이디] 에 해당하는 폴더를 꼭 먼저 만들어 주시고, 해당 폴더 안에서 작업을 진행해 주세요.

# week1 : djagno tutorial part1 ~ part4

## part 1

```python
# mysite/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

- include() 함수는 다른 URLconf들을 참조할 수 있도록 도와준다.
- path() 인수 :
    - route : `route` 는 URL 패턴을 가진 문자열
    - name : URL에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조 가능. 이 강력한 기능을 이용하여, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있도록 도와줌.



## part2

```python
## polls/models.py

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

몇몇 Field 클래스들은 필수 인수가 필요하다. 예를 들어, CharField는 max_length를 입력해야 함.



django는 migrate를 하게 되면, 기본 키 (ID)가 자동으로 추가된다. 관례에 따라, Django는 외래 키 필드명에 "`_id`" 이름을 자동으로 추가한다.



## part3

### 지름길 : render()

템플릿에 context를 채워넣어 표현한 결과를 `HttpResponse`  객체와 함께 돌려주는 구문은 자주 쓰는 용법이다. 따라서, Django는 이런 표현을 쉽게 표현할 수 있도록 단축 기능(shortcuts)을 제공한다.

```python
## polls/views.py

from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

render() 함수는

- 첫번째 인수 : request 객체
- 두번째 인수 : 템플릿 이름
- 세번째 인수 (선택적) : context 사전형 객체

를 인수로 받는다. 인수로 지정된 context로 표현된 템플릿의 `HttpResponse` 객체가 반환된다.



### 지름길 : get_object_or_404()

만약 객체가 존재하지 않을 때 get()을 사용하여 Http404 예외를 발생시키는 것은 자주 쓰이는 용법이다. Django에서 이 기능에 대한 단축 기능을 제공한다.

```python
## polls/views.py

from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

get_object_or404() 함수는

- 첫번째 인수 : Django 모델
- n번째 인수 : 몇 개의 키워드 인수

를 인수로 받는다.  `get_object_or_404()` 함수처럼 동작하는 `get_list_or_404()`함수가 있다. [`get()`](https://docs.djangoproject.com/ko/3.1/ref/models/querysets/#django.db.models.query.QuerySet.get) 대신 [`filter()`](https://docs.djangoproject.com/ko/3.1/ref/models/querysets/#django.db.models.query.QuerySet.filter) 를 쓴다는 것이 다르다.



## part4

- GET과 POST의 차이
    - HTTP
        - http는 웹상에서 클라이언트와 서버 간에 요청/응답으로 데이터를 주고 받을 수 있는 프로토콜이다. 
        - 클라이언트가 http 프로토콜을 통해 서버에게 요청을 보내면 서버는 요청에 맞는 응답을 클라이언트에게 전송
        - 이 때, http 요청에 포함되는 http 메소드는 서버가 요청을 수행하기 위해 해야할 행동을 표시하는 용도로 사용된다.
        - 이 http 메소드 중 GET과 POST이 있는 것.
    - GET
        - GET은 요청을 전송할 때 필요한 데이터를 Body에 담지 않고, 쿼리스트링을 통해 전송한다.
        - 쿼리 스트링 : URL의 끝에 `?`와 함께 이름과 값으로 쌍을 이루는 요청 파라미터
        - 요청 파라미터가 여러 개이면 `&`로 연결한다. 
        - 쿼리스트링을 사용하게 되면, URL에 조회 조건을 표시한다.
    - POST
        - POST는 **리소스를 생성/변경하기 위해 설계**되었기 때문에 GET과 달리 전송해야될 데이터를 HTTP 메세지의 Body에 담아서 전송한다.
        - HTTP 메세지의 Body는 길이의 제한 없이 데이터를 전송할 수 있다.
        - 그래서 POST 요청은 GET과 달리 대용량 데이터를 전송할 수 있다.
        - GET보다 보안적인 면에서 비교적 안전하다. (그러나, POST 요청도 크롬 개발자 도구, Fiddler와 같은 툴로 요청 내용을 확인할 수 있기 때문에 민감한 데이터는 반드시 암호화해야 한다.)
        - POST로 요청을 보낼 때는 요청 헤더의 Content-Type에 요청 데이터의 타입을 표시해야 한다.
        - 데이터 타입을 표시하지 않으면 서버는 내용이나 URL에 포함된 리소스의 확장자명 등으로 데이터 타입을 유추한다.



```python
## polls/views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

- `request.POST`는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 객체이다. 이 경우, `request.POST['choice']`는 선택된 설문의 ID를 문자열로 반환한다.
- `request.POST`의 값은 항상 문자열
- 설문지의 수가 증가한 이후에, 코드는 일반 `HttpResponse`가 아닌 `HttpResponseRedirect`를 반환하고, `HttpResponseRedirect`는 하나의 인수를 받는다.
    - render와 redirect의 구분
        - render : 템플릿을 불러옴
        - redirect : URL로 이동함
- 그 인수는 사용자가 재전송될 URL
- `reverse()` : URL을 하드코딩하지 않도록 도와준다.



### 제너릭 뷰 사용하기

```python
## polls/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```

- ListView : 개체 목록 표시
- DetailView : 특정 개체 유형에 대한 세부 정보 페이지 표시

각각 , 이 개념을 추상화한다.