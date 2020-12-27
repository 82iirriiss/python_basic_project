from django.db import models


# Create your models here.
# Question 테이블의 PK : 장고는 자동으로 Not Null & Autoincrement인 id 를 만들어 줌
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # DateTimeField의 'date published' 는 pub_date에 대한 레이블 문구. Admin 사이트에서 볼 수 있음.
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # 항상 인수로 전달된 테이블의 PK 와 연결됨. 실제 테이블에는 '_id' 라는 접미사가 붙음
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
