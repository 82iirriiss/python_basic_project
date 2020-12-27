from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.views import generic

import logging

logger = logging.getLogger(__name__)
# logger = logging.getLogger(__name__)
# Create your views here.
# def index(request):
#     # Question 테이블 객체에서 pub_date 컬럼의 역순으로 정렬하여 5개의 최근 Question 객체를 가져옴
#     latest_question_list = Question.objects.all()
#     print(latest_question_list)
#     context = {'latest_question_list': latest_question_list}
#     # render() 는 context를 인자로 받아 HTTPResponse를 반환함
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    # 템플릿 파일명과 컨텍스트 변수명은 지정을 해도 되고, 디폴트 값을 사용 할 수도 있다.
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # 테이블의 모든 데이터를 조회하려면 'model=Question' 만 해주면 되나, 더 자세한 쿼리를 하려면 get_queryset을 오버라이딩 해야함
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):

    logger.debug("vote().question_id: %s" % question_id)
    # logger.debug("vote().question_id: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': "You didn't select a choice."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다리엑션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
