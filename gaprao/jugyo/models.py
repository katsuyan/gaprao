from django.db import models
from django.contrib.auth.models import User



class Jugyo(models.Model):
    """授業"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('授業名', max_length=255)
    room = models.CharField('教室', max_length=255)
    syllabus_url = models.CharField('シラバスURL', max_length=255)
    term = models.CharField('学期', max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Year(models.Model):
    """年度"""
    id = models.AutoField(primary_key=True)
    jugyo = models.ManyToManyField(Jugyo, verbose_name='授業', related_name='years')
    year = models.IntegerField('年度')

    def __str__(self):
        return str(self.year)


class Exam(models.Model):
    """テスト"""
    id = models.AutoField(primary_key=True)
    jugyo = models.ForeignKey(Jugyo, verbose_name='授業', related_name='exams')
    name = models.CharField('テスト名', max_length=255)
    day = models.DateField('テスト日')
    exam_info = models.TextField('テスト範囲')

    def __str__(self):
        return self.jugyo.name


class NoJugyo(models.Model):
    """休講"""
    id = models.AutoField(primary_key=True)
    jugyo = models.ForeignKey(Jugyo, verbose_name='授業', related_name='no_jugyos')
    day = models.DateField('休講日')

    def __str__(self):
        return self.jugyo.name

class UpJugyo(models.Model):
    """補講"""
    id = id = models.AutoField(primary_key=True)
    jugyo = models.ForeignKey(Jugyo, verbose_name='授業', related_name='up_jugyos')
    day = models.DateField('補講日')

    def __str__(self):
        return self.jugyo.name


class Homework(models.Model):
    """課題"""
    id = models.AutoField(primary_key=True)
    jugyo = models.ForeignKey(Jugyo, verbose_name='授業', related_name='homeworks')
    name = name = models.CharField('課題名', max_length=255)
    dead_line = models.DateField('締め切り')
    info = models.TextField('課題内容')

    def __str__(self):
        return self.jugyo.name


class Teacher(models.Model):
    """教師"""
    id = models.AutoField(primary_key=True)
    jugyos = models.ManyToManyField(Jugyo, verbose_name='授業', related_name='teachers')
    name = name = models.CharField('名前', max_length=255)

    def __str__(self):
        return self.name


class JugyoDateTime(models.Model):
    """授業日授業時間"""
    id = models.AutoField(primary_key=True)
    jugyos = models.ManyToManyField(Jugyo, verbose_name='授業', related_name='date_times')
    date = models.IntegerField('曜日')
    period = models.IntegerField('時限')

    def __str__(self):
        return str(self.date)


class Comment(models.Model):
    """コメント"""
    id = models.AutoField(primary_key=True)
    jugyo = models.ForeignKey(Jugyo, verbose_name='授業', related_name='comments')
    comment = models.TextField('コメント')

    def __str__(self):
        return self.jugyo.name

class MyPage(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='ユーザ')
    jugyo = models.ForeignKey(Jugyo, verbose_name='授業')

    def __str__(self):
        return str(self.id)
