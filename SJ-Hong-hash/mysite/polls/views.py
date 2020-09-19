# view는 django app이 특정 기능과 템플릿을 제공하는 웹 페이지의 한 종류인 공개 인터페이스이다.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    # polls/index.html에서 template을 불러온 후, 해당 context를 전달한다.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
# render을 이용하면 index함수를 더 단순하게 할 수 있다.
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)