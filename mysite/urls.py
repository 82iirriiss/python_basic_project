"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite import views


# URL 패턴 매칭이 위에서 아래로 진행되므로, 순서에 유의 해야 함
# path() 함수는, route, view 2개의 필수 인자와 kwargs, name 2개의 선택 인자를 받음
#   route: URL 스트링
#   view: 호출되는 뷰 함수
#   kwargs: URL에서 추출된 파라미터 외에 추가적인 파라미터를 함수에 전달 할때 사용
#   name: 각 URL 패턴별로 이름을 붙여줌. 이 이름을 Templete 에서 많이 사용함.
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('books/', include('books.urls')),
    # path('polls/', views.index, name='index'),
    # path('polls/<int:question_id>/', views.detail, name='detail'),
    # path('polls/<int:question_id>/vote/',views.vote, name='vote'),
    # path('polls/<int:question_id>/results/',views.results, name='results'),

]
