# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class string_with_title(str):
    """ 用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,
    所以修改str类的title方法就可以实现.
    """
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

# Create your models here.
STATUS = {
        0: u'正常',
        1: u'草稿',
        2: u'删除',
}

# 资讯来源
NEWS = {
        0: u'oschina',
        1: u'chiphell',
        2: u'freebuf',
        3: u'cnBeta',
}


class content_type(models.Model):
    app_label = models.CharField(max_length=40, verbose_name=u'名称')
    model = models.CharField(max_length=40, verbose_name=u'数据库名称')

    def __unicode__(self):
        return '%s' % (self.app_label)

    __str__ = __unicode__


