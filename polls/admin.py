from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline): # Question, Choice 한 화면에서 보기
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text'] # 필드 순서 변경
    fieldsets = [('Question Statement', {'fields':['question_text']}), # 필드 분리하여 보여주기
                 ('Date Information', {'fields':['pub_date'],'classes':['collapse']}),] # 필드 펼치기 기능  추가
    inlines = [ChoiceInline] # Choice 모델 클래스 같이 보기
    list_display = ('question_text','pub_date') # 레코드 리스트 컬럼 지정하기
    list_filter = ['pub_date'] # 리스트 필터 지정하기
    search_fields = ['question_text'] # 레코드 검색 필드 추가하기

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)