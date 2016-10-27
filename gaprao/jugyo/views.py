"""
File Name   : view.py
Designer	: 田島 克哉
Date		: 2016.06.27
Purpose   	: 授業共有サービスメインview
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from jugyo.models import Jugyo, MyPage, JugyoDateTime, Teacher, Year, NoJugyo, UpJugyo, Homework, Exam
from django.views.decorators.csrf import ensure_csrf_cookie
import datetime
import json

import logging
logger = logging.getLogger('command')


"""
Function Name       : entory()
Designer            : 田島 克哉
Last Updated		: 2016.6.27
Function            : 授業追加画面作成
Return              : template
"""
@login_required
@ensure_csrf_cookie
def index(request):
    """授業一覧"""
    jugyos = Jugyo.objects.all().order_by("id")
    date_list = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"]
    data_list = []
    for jugyo in jugyos:
        year = jugyo.years.all().order_by("id")[0]
        teacher = jugyo.teachers.all().order_by("id")[0]
        date_time = jugyo.date_times.all().order_by("id")[0]


        data = {"id": jugyo.id, "name": jugyo.name, "year": year.year, "teacher": teacher.name, "date": date_list[date_time.date], "period": date_time.period }
        data_list.append(data)

    return render(request, 'jugyo/index.html', {"data_list": data_list})

"""
Function Name       : entory()
Designer            : 田島 克哉
Last Updated		: 2016.6.27
Function            : 授業追加画面作成
Return              : template
"""
@login_required
def entory(request):
    return render(request, 'jugyo/entory.html')


"""
Function Name       : create
Designer            : 田島 克哉
Last Updated		: 2016.6.28
Function            : 授業追加処理
Return              : json
"""
@login_required
def create(request):
    name = request.POST['name']
    room = request.POST['room']
    syllabus_url = request.POST['syllabus_url']
    term = request.POST['term']
    year = request.POST['year']
    teacher = request.POST['teacher']
    date = request.POST['date']
    period = request.POST['period']
    nojugyo_list = request.POST.getlist('nojugyo_list[]')
    upjugyo_list = request.POST.getlist('upjugyo_list[]')
    homework_list = request.POST.getlist('homework_list[]')
    exam_list = request.POST.getlist('exam_list[]')

    update_jugyo = Jugyo(name=name, room=room, syllabus_url=syllabus_url, term=term)
    update_jugyo.save()

    new_year = Year(year=int(year))
    new_year.save()
    new_year.jugyo.add(update_jugyo)

    new_teacher = Teacher(name=teacher)
    new_teacher.save()
    new_teacher.jugyos.add(update_jugyo)

    update_jugyo_date_time = JugyoDateTime(date=date, period=period)
    update_jugyo_date_time.save()
    update_jugyo_date_time.jugyos.add(update_jugyo)

    for nojugyo in nojugyo_list:
        nojugyo_datetime = datetime.datetime.strptime(nojugyo, '%Y/%m/%d')
        new_nojugyo = NoJugyo(jugyo_id=update_jugyo.id, day=nojugyo_datetime)
        new_nojugyo.save()

    for upjugyo in upjugyo_list:
        upjugyo_datetime = datetime.datetime.strptime(upjugyo, '%Y/%m/%d')
        new_upjugyo = UpJugyo(jugyo_id=update_jugyo.id, day=upjugyo_datetime)
        new_upjugyo.save()

    for homework_json in homework_list:
        homework = json.loads(homework_json)
        dead_line = datetime.datetime.strptime(homework['dead_line'], '%Y/%m/%d')
        new_homework = Homework(jugyo_id=update_jugyo.id,
                                name=homework['name'],
                                dead_line=dead_line,
                                info=homework['info'])
        new_homework.save()

    for exam_json in exam_list:
        exam = json.loads(exam_json)
        day = datetime.datetime.strptime(exam['day'], '%Y/%m/%d')
        new_exam = Exam(jugyo_id=update_jugyo.id,
                        name=exam['name'],
                        day=day,
                        exam_info=exam['exam_info'])
        new_exam.save()

    data = {'text': '授業を作成しました。', 'redirect_url': '/jugyo/index'}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)


"""
Function Name       : edit()
Designer            : 佐久間 隆平
Last Updated		: 2016.6.27
Function            : 授業編集画面作成
Return              : template
"""
@login_required
@ensure_csrf_cookie
def edit(request, jugyo_id):
    exist_jugyo = Jugyo.objects.filter(id=jugyo_id)[0]
    exist_name = exist_jugyo.name
    exist_room = exist_jugyo.room
    exist_term = exist_jugyo.term
    exist_syllabus_url = exist_jugyo.syllabus_url
    exist_year = exist_jugyo.years.all().order_by('id')[0]
    exist_teacher = exist_jugyo.teachers.all().order_by('id')[0]
    exist_date_time = exist_jugyo.date_times.all().order_by('id')[0]
    exist_exams = exist_jugyo.exams.all().order_by('id')
    exist_homeworks = exist_jugyo.homeworks.all().order_by('id')
    exist_upjugyos = exist_jugyo.up_jugyos.all().order_by('id')
    exist_nojugyos = exist_jugyo.no_jugyos.all().order_by('id')

    data = {"jugyo_id" :jugyo_id,
            "name": exist_name,
            "room": exist_room,
            "term": exist_term,
            "syllabus_url": exist_syllabus_url,
            "year": exist_year.year,
            "teacher": exist_teacher.name,
            "date": exist_date_time.date,
            "period": exist_date_time.period}

    return render(request,'jugyo/edit.html',
                    {"data": data, "exams": exist_exams, "homeworks": exist_homeworks, "upjugyos": exist_upjugyos, "nojugyos": exist_nojugyos})


"""
Function Name       : update()
Designer            : 佐久間 隆平
Last Updated		: 2016.6.27
Function            : 授業更新処理
Return              : json
"""
@login_required
def update(request, jugyo_id):
    name = request.POST.get('name', False)
    room = request.POST.get('room', False)
    syllabus_url = request.POST.get('syllabus_url', False)
    term = request.POST.get('term', False)
    year = request.POST.get('year', False)
    teacher = request.POST.get('teacher', False)
    date = request.POST.get('date', False)
    period = request.POST.get('period', False)
    nojugyo_list = request.POST.getlist('nojugyo_list[]')
    upjugyo_list = request.POST.getlist('upjugyo_list[]')
    homework_list = request.POST.getlist('homework_list[]')
    exam_list = request.POST.getlist('exam_list[]')


    update_jugyo = get_object_or_404(Jugyo, pk=jugyo_id)
    update_jugyo.name = name
    update_jugyo.room = room
    update_jugyo.syllabus_url = syllabus_url
    update_jugyo.term = term
    update_jugyo.save()

    new_year = get_object_or_404(Year, jugyo=update_jugyo)
    new_year.year = int(year)
    new_year.save()

    new_teacher = get_object_or_404(Teacher, jugyos=update_jugyo)
    new_teacher.name = teacher
    new_teacher.save()

    update_jugyo_date_time = get_object_or_404(JugyoDateTime, jugyos=update_jugyo)
    update_jugyo_date_time.date = date
    update_jugyo_date_time.period = period
    update_jugyo_date_time.save()

    NoJugyo.objects.filter(jugyo=update_jugyo).delete()
    for nojugyo in nojugyo_list:
        nojugyo_datetime = datetime.datetime.strptime(nojugyo, '%Y/%m/%d')
        new_nojugyo = NoJugyo(jugyo_id=update_jugyo.id, day=nojugyo_datetime)
        new_nojugyo.save()

    UpJugyo.objects.filter(jugyo=update_jugyo).delete()
    for upjugyo in upjugyo_list:
        upjugyo_datetime = datetime.datetime.strptime(upjugyo, '%Y/%m/%d')
        new_upjugyo = UpJugyo(jugyo_id=update_jugyo.id, day=upjugyo_datetime)
        new_upjugyo.save()

    Homework.objects.filter(jugyo=update_jugyo).delete()
    for homework_json in homework_list:
        homework = json.loads(homework_json)
        dead_line = datetime.datetime.strptime(homework['dead_line'], '%Y/%m/%d')
        new_homework = Homework(jugyo_id=update_jugyo.id,
                                name=homework['name'],
                                dead_line=dead_line,
                                info=homework['info'])
        new_homework.save()

    Exam.objects.filter(jugyo=update_jugyo).delete()
    for exam_json in exam_list:
        exam = json.loads(exam_json)
        day = datetime.datetime.strptime(exam['day'], '%Y/%m/%d')
        new_exam = Exam(jugyo_id=update_jugyo.id,
                        name=exam['name'],
                        day=day,
                        exam_info=exam['exam_info'])
        new_exam.save()

    data = {'text': '授業を編集しました。', 'redirect_url': '/jugyo/index'}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)



"""
Function Name       : delete()
Designer            : 染谷 祐理子
Last Updated		: 2016.6.27
Function            : 授業削除処理
Return              : template
"""
@login_required
def delete(request, jugyo_id):
    """授業の削除"""
    jugyo = get_object_or_404(Jugyo, pk=jugyo_id)
    jugyo.delete()
    return redirect('index')
    jugyos = Jugyo.objects.all().order_by('id')
    return render(request, 'jugyo/index.html', {'jugyos': jugyos})


"""
Function Name       : detail()
Designer            : 吉野 朱音
Last Updated		: 2016.6.27
Function            : 授業詳細画面作成処理
Return              : template
"""
@login_required
@ensure_csrf_cookie
def detail(request, jugyo_id=None):
    date_list = ["月曜", "火曜", "水曜", "木曜", "金曜", "土曜"]
    jugyo = Jugyo.objects.filter(id=jugyo_id)

    jugyo = jugyo[0]
    jugyo_id = jugyo.id
    name = jugyo.name
    room = jugyo.room
    term = jugyo.term
    syllabus_url = jugyo.syllabus_url
    year = jugyo.years.all().order_by('id')[0]
    teacher = jugyo.teachers.all().order_by('id')[0]
    date_time = jugyo.date_times.all().order_by('id')[0]
    exams = jugyo.exams.all().order_by('id')
    homeworks = jugyo.homeworks.all().order_by('id')
    upjugyos = jugyo.up_jugyos.all().order_by('id')
    nojugyos = jugyo.no_jugyos.all().order_by('id')

    data = {"jugyo_id" :jugyo_id,
            "name": name,
            "room": room,
            "term": term,
            "syllabus_url": syllabus_url,
            "year": year.year,
            "teacher": teacher.name,
            "date": date_list[date_time.date],
            "period": date_time.period}
    return render(request,'jugyo/detail.html',
                    {"data": data, "exams": exams, "homeworks": homeworks, "upjugyos": upjugyos, "nojugyos": nojugyos})


"""
Function Name       : add_mypage
Designer            : 友成 順也
Last Updated		: 2016.6.28
Function            : Myページ授業追加処理
Return              : json
"""
@login_required
def add_mypage(request):
    jugyo_id = request.POST['jugyo_id']
    user = request.user
    jugyo = Jugyo.objects.filter(id=jugyo_id)[0]

    date_time = jugyo.date_times.all().order_by('id')[0]
    date = date_time.date
    period = date_time.period

    my_jugyos = MyPage.objects.filter(user=user)

    for my_jugyo in my_jugyos:
        my_jugyo_date_time = my_jugyo.jugyo.date_times.all().order_by('id')[0]
        my_jugyo_date = my_jugyo_date_time.date
        my_jugyo_period = my_jugyo_date_time.period
        if(date == my_jugyo_date and period == my_jugyo_period):
            my_jugyo.delete()

    new_my_jugyo = MyPage.objects.create(user=user, jugyo=jugyo)
    new_my_jugyo.save()
    data = {'text': "追加が完了しました。", 'redirect_url': '/'}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)


"""
Function Name       : my_page()
Designer            : 友成 順也
Last Updated		: 2016.6.28
Function            : Myページ画面作成処理
Return              : json
"""
@login_required
@ensure_csrf_cookie
def my_page(request):
    """Myページ"""
    monday = [None, None, None, None, None, None]
    tuesday = [None, None, None, None, None, None]
    wednesday = [None, None, None, None, None, None]
    thursday = [None, None, None, None, None, None]
    friday = [None, None, None, None, None, None]
    saturday = [None, None, None, None, None, None]

    user = request.user
    mypages = MyPage.objects.filter(user=user)
    for mypage in mypages:
        date_time = mypage.jugyo.date_times.all().order_by('id')[0]
        jugyo = {'id'  : mypage.jugyo.id,
                 'name': mypage.jugyo.name,
                 'room': mypage.jugyo.room}
        if date_time.date == 0:
            monday[date_time.period - 1] = jugyo
        elif date_time.date == 1:
            tuesday[date_time.period - 1] = jugyo
        elif date_time.date == 2:
            wednesday[date_time.period - 1] = jugyo
        elif date_time.date == 3:
            thursday[date_time.period - 1] = jugyo
        elif date_time.date == 4:
            friday[date_time.period - 1] = jugyo
        elif date_time.date == 5:
            saturday[date_time.period - 1] = jugyo
    return render(request, 'jugyo/my_page.html', {'monday': monday,
                                                  'tuesday': tuesday,
                                                  'wednesday': wednesday,
                                                  'thursday': thursday,
                                                  'friday': friday,
                                                  'saturday': saturday})

"""
Function Name       : my_page()
Designer            : 友成 順也
Last Updated		: 2016.6.28
Function            : Myページ削除処理
Return              : json
"""
def delete_myjugyo(request):
    user = request.user
    jugyo_id = request.POST['id']
    jugyo = Jugyo.objects.filter(id=jugyo_id)[0]

    del_myjugyo = MyPage.objects.filter(user=user, jugyo=jugyo)
    del_myjugyo.delete()

    data = {'text': "削除しました"}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
