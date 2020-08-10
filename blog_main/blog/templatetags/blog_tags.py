from ..models import Post, Category, Tag
from django import template

register = template.Library()


# 获取最近几条博客
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


# 归档模板标签，按照月份
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()


# 标签云
@register.simple_tag
def get_tags(pk):
    if pk:
        post = Post.objects.get(pk=pk)
        if post:
            return post.tags
        else:
            raise
    else:
        raise
