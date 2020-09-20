from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # pk: question_id
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    # detail, results를 볼 때 똑같이 question_id 패턴이 들어가므로 이걸 기본키로 바꿔준다.
    # 다만, vote에서도 question_id 대신 pk를 적을 경우 pk가 무엇인지 모르기 때문에 에러가 발생한다.
    # unexpected argument 'pk'라는 에러
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
