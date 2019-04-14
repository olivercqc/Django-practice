from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要 可以为空 但是CharField默认要求存入数据 不然会报错
    # 指定blank=True就可以允许空值了
    excerpt = models.CharField(max_length=200, blank=True)

    # 将文章对应的数据库表和分类、标签对应的数据库表关联了起来
    # 一篇文章只能对应一个分类 但是一个分类下可以有多篇文章 所以使用ForeignKey 即一对多的关系
    # 一篇文章可以有多个标签 同一个标签下可有多篇文章 使用ManyToManyField 表示多对多的关系
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # djang.contrib.auth是Django内置的应用 专门用来处理网站用户的注册 登陆等流程
    # 一篇文章只能有一个作者 一个作则可能会写多篇文章 一对多的关系 使用ForeignKey
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
