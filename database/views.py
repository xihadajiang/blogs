# -*- coding: utf-8 -*-
from django import template
from django import forms
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template import Context, loader
from django.views.generic import View, TemplateView, ListView, DetailView
from django.db.models import Q
from django.core.cache import caches
from django.core.exceptions import PermissionDenied
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from blog.models import Article, Category, Carousel, Column, Nav, News
from vmaig_comments.models import Comment
from vmaig_auth.models import VmaigUser
from vmaig_system.models import Link
from vmaig_auth.forms import VmaigUserCreationForm, VmaigPasswordRestForm
from django.conf import settings
import datetime
import time
import json
import logging

# 缓存
try:
    cache = caches['memcache']
except ImportError as e:
    cache = caches['default']

# logger
logger = logging.getLogger(__name__)


class DataControl(View):
    print 'View'
    def post(self, request, *args, **kwargs):
        # 获取要对用户进行什么操作
        slug = self.kwargs.get('slug')

        if slug == 'login':
            return self.login(request)
        elif slug == "logout":
            return self.logout(request)
        elif slug == "register":
            return self.register(request)
        elif slug == "changepassword":
            return self.changepassword(request)
        elif slug == "forgetpassword":
            return self.forgetpassword(request)
        elif slug == "changetx":
            return self.changetx(request)
        elif slug == "resetpassword":
            return self.resetpassword(request)
        elif slug == "notification":
            return self.notification(request)

        raise PermissionDenied

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')

        if slug == 'select':
            return self.select(request)
        elif slug == "all":
            return self.all(request)
        elif slug == "register":
            return self.register(request)
        elif slug == "changepassword":
            return self.changepassword(request)
        elif slug == "forgetpassword":
            return self.forgetpassword(request)
        elif slug == "changetx":
            return self.changetx(request)
        elif slug == "resetpassword":
            return self.resetpassword(request)
        elif slug == "notification":
            return self.notification(request)

        raise PermissionDenied
        raise Http404
    def select(self, request):
        username = request.GET.get("username", "")
        password = request.GET.get("password", "")

        errors = []

        errors.append(u"密码或者用户名不正确")

        mydict = {"errors": errors}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )
    def all(self, request):
        html = ""
        isend = False
        article_list =['1']
        for article in article_list:
            html += template.loader.get_template(
                        'blog/include/all_post.html'
                    ).render(template.Context({'post': article}))

        mydict = {"html": html, "isend": isend}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )
