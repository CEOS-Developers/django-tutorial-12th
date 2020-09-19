# view는 django app이 특정 기능과 템플릿을 제공하는 웹 페이지의 한 종류인 공개 인터페이스이다.

from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Question, Choice


# Create your views here.
def index(request):
    # polls/index.html에서 template을 불러온 후, 해당 context를 전달한다.
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# vote가 끝나면 결과 페이지로 리다이렉트
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST['choice']를 기본 키로 갖는 qustion의 choice를 선택함
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # vote를 안한 경우 KeyError를 내고 다시 polls/detail.html로 돌아감
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    # vote를 시행한 경우
    else:
        # 해당 choice가 얻은 득표수 1 증가 및 저장
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # 리다이렉션을 걸어둠
        # POST가 성공적으로 실행된다면, HttpResponse가 아닌 HttpResponseRedirect로 반환해야 한다. 이유는 위에 영어 주석
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))