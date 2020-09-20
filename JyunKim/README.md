# Django
## 1주차
### part1
- git, 기본 환경 세팅  
- 프로젝트, 앱 생성
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
] 
```
프로젝트에 앱 추가
- request -> mysite.urls(최상위 urlconfig) -> polls.urls -> views   
```
# mysite.urls.py

urlpatterns = [   
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),   
]
```
### part2
- DB연동
```
# mysite.settings.py

DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'mysql.cnf'),
        }
    }
}
```
- 모델 생성 및 활성화
```
# polls.models.py

class Choice(models.Model):
    # ForeignKey - Choice.question <-> Question.choices.~
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# manage.py makemigrations polls - 변경 사항 저장
# manage.py migrate - db에 적용
```
- timezone
```
# mysite.settings.py

TIME_ZONE = 'Asia/Seoul'
USE_TZ = True
```
DB에는 기준 시간(UTC)로 저장되고 템플릿, 폼에서는 사용자 시간으로 나타남
- 관리자 사이트
```
# polls.admin.py

admin.site.register(Question)
admin.site.register(Choice)
# python manage.py createsuperuser - 관리자 생성
```
관리할 모델 추가
### part3
- url
```
# polls.urls.py

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
path(route, view, kwargs, name)
```
# polls.templates.polls.index.html

<a href="{% url 'polls:detail' question.id %}">
```
하드코팅된 url 대신 'app_name:name' 으로 호출 가능
- 뷰, 렌더링
```
# polls.view.py

context = {'question': question, 'error_message': "You didn't select a choice."}
        return render(request, 'polls/detail.html', context)
```
HttpResponse 객체 반환
### part4
- post, 리디렉션   
```
# polls.views.py

selected_choice = question.choices.get(pk=request.POST['choice'])
return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
```
POST 처리 완료하면 redirect 해줘야 함(뒤로가기 눌렀을 때 데이터가 두번 post 되는 것 방지)   
reverse: url name으로 접근 가능
- 제네릭 뷰
```
# polls.views.py

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # 최근게 앞에 오도록 정렬
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
```
변수, 함수 override
- 암호 분리
```
# mysite.settings.py

secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

SECRET_KEY = secrets["SECRET_KEY"]
```
- 커밋 메시지 수정   
-> 동사원형으로 시작해서 명령문으로 작성