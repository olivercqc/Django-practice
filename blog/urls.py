#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 该文件用于blog应用相关的url配置
# 将不同的网址对应的处理函数写在一个urls.py文件里，当用户访问某个网址时，Django就会去这个文件找
# 如果找到这个网址，就会调用和它绑定在一起的处理函数(叫做视图函数)
from django.conf.urls import url

from . import views

urlpatterns = [
    # 把网址和对应的处理函数作为参数传给url函数 第一个参数是网址 第二个参数是处理函数
    # name作为处理函数index的别名，以后会用到
    # ^$表示以空字符串开头并且以空字符串结尾
    url(r'^$', views.index, name='index'),
]