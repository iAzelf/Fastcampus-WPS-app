from django.db import models
from fastcampus.models import BaseModel


class Course(BaseModel):
    CHOICES_TYPE = (
        ('school', 'School과정'),
        ('camp', 'Camp과정'),
    )

    type = models.CharField('과정 분류', max_length=20, choices=CHOICES_TYPE)
    title = models.CharField('과정 이름', max_length=50)
    number = models.IntegerField('기수', default=0)
    description = models.CharField('간단설명', max_length=100)
    start_date = models.DateField('과정 시작일')
    end_date = models.DateField('과정 종료일')

    def __str__(self):
        return self.full_title

    @property
    def full_title(self):
        return '%s %s기' % (self.title, self.number)


class LectureVideo(BaseModel):
    course = models.ForeignKey(Course, verbose_name='해당 코스')
    title = models.CharField('강의 제목', max_length=100)
    description = models.CharField('설명', max_length=200, blank=True)
    youtube_url = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title
