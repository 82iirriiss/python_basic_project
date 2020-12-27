from django.urls import path
from . import views

# URL 패턴 매칭이 위에서 아래로 진행되므로, 순서에 유의 해야 함
# path() 함수는, route, view 2개의 필수 인자와 kwargs, name 2개의 선택 인자를 받음
#   route: URL 스트링
#   view: 호출되는 뷰 함수
#   kwargs: URL에서 추출된 파라미터 외에 추가적인 파라미터를 함수에 전달 할때 사용
#   name: 각 URL 패턴별로 이름을 붙여줌. 이 이름을 Templete 에서 많이 사용함.
# app_name 은, URL가 중복되는 경우 네임스페이스를 구별해 줌 (예를 들어, polls 애플리케이션과 임의의 blogs 라는 애플리케이션이 'detail' 이라는 url 패턴을 갖는 경우,)
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),                                # /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),            # /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # /polls/5/results
    path('<int:question_id>/vote/', views.vote, name='vote'),            # /polls/5/vote/
]