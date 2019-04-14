#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 该文件用于blog应用相关的url配置
# 将不同的网址对应的处理函数写在一个urls.py文件里，当用户访问某个网址时，Django就会去这个文件找
# 如果找到这个网址，就会调用和它绑定在一起的处理函数(叫做视图函数)
from django.conf.urls import url
from . import views

# 通过app_name = 'blog'告诉Django这个urls.py模块是属于blog应用的
# 这种技术叫做视图函数命名空间
app_name = 'blog'

urlpatterns = [
    # 把网址和对应的处理函数作为参数传给url函数 第一个参数是网址 第二个参数是处理函数
    # name作为处理函数index的别名，以后会用到
    # ^$表示以空字符串开头并且以空字符串结尾
    url(r'^$', views.index, name='index'),
    # (?P<pk>[0-9+])表示命名捕获组
    # 作用是从用户访问的URL里把括号内匹配的字符串捕获并作为关键字参数传给其对应的视图函数detail
    # 例如：当用户访问post/255/时(Django并不关心域名, 而只关心去掉域名后的相对URL)
    # 被括起来的部分(?P<pk>[0-9]+)匹配255
    # 这个255会在调用视图函数detail时被传递进去
    # 实际上就是detail(request, pk=255)
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
