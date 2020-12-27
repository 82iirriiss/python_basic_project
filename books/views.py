from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher

# Create your views here.

# 템플릿 뷰만 모델링하여 사용하는 경우 TemplateView 사용
class BooksModelView(TemplateView):
    # template_name 오버라이드 필수
    template_name = 'books/index.html'

    # 템플릿 파일에 넘겨줘야 할 데이터가 있는경우 get_context_data 오버라이드
    def get_context_data(self, **kwargs):
        # get_context_data를 오버라이드 할때는 반드시 첫줄에 super() 메소드를 호출해야 한다.
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context


class BookList(ListView):
    # model 테이블에 들어있는 모든 레코드를 가져와 구성하는 경우에는 테이블명만 지정해 주면 된다.
    # object_list 속성 자동구성
    # 템플릿 파일 모델명_list.html 자동구성
    model = Book

class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    model = Publisher

# pk로 조회해서 특정 객체를 가져오는 경우에는 테이블명만 명시 해주면 된다.
# 컨텍스트 변수로 object 를 자동으로 사용함
# 템플릿 파일을 모델명_detail.html 로 자동으로 사용함
class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher