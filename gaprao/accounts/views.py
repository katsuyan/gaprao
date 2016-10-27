"""
File Name   : view.py
Designer	: 田島 克哉
Date		: 2016.06.27
Purpose   	: アカウント関係のview
"""

from django.shortcuts import render
from django.shortcuts import loader
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
import json

import logging
logger = logging.getLogger('command')

"""
Function Name       : login()
Designer            : 田島 克哉
Last Updated		: 2016.6.27
Function            : 承認処理
Return              : template
"""
@ensure_csrf_cookie
def login(request):
    from django.contrib.auth import login

    user = None  # GET時のNameErrorを防ぐための仮定義

    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']
        user = authenticate(username=uname, password=pword)

        if user is not None:
            if user.is_active:
                login(request, user)
                data = {'redirect_url': '/'}
                json_str = json.dumps(data, ensure_ascii=False, indent=2)
                return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)

    contexts = RequestContext(request, {
        'request':request.method,
        'user':user,
    })
    template = loader.get_template('accounts/login.html')

    return HttpResponse(template.render(contexts))


"""
Function Name       : create_user()
Designer            : ユーザ登録処理
Last Updated		: 2016.6.27
Function            : 承認処理
Return              : template
"""
def create_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    registered_user = User.objects.all().order_by("id")
    logger.info(registered_user)
    for user in registered_user:
        if user.username == username:
            data = {'success': False, 'redirect_url': '#', 'text': 'このユーザ名はすでに使用されています。'}
            json_str = json.dumps(data, ensure_ascii=False, indent=2)
            return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
        elif user.email == email:
            data = {'success': False, 'redirect_url': '#', 'text': "このメールアドレスはすでに登録されています。"}
            json_str = json.dumps(data, ensure_ascii=False, indent=2)
            return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)

    new_user = User.objects.create_user(username, email, password)
    new_user.save()

    data = {'success': True, 'redirect_url': '/login', 'text': "登録が完了しました。ログイン画面からログインしてください。"}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)
