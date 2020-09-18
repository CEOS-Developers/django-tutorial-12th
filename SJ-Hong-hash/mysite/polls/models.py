import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# 데이터베이스의 각 필드는 Field 클래스의 인스턴스로 표현된다.
# Question class has a question & a publication date
class Question(models.Model):
    # Define data needed
    # CharField represents on Character field
    # 어떤 Field 클래스를 정의할 때 포함시켜야 할 필요요소가 있는데, CharField는 max_length가 필요하다.
    question_text = models.CharField(max_length=200)
    # DataTimeField represents on date and time
    pub_date = models.DateTimeField('date published')

    # 만일 behavior도 정의하고 싶다면 def를 사용해 정의하면 된다.
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Choice class has two fields: text of choices & vote
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # IntegerField의 default는 votes의 기본값을 0으로 설정한다는 뜻
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
