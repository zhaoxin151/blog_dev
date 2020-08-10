import sys
from django.shortcuts import render
from django.http import Http404
from .models import Post
import markdown
# Create your views here.

sys.path.append("..")

from comments.forms import CommentForm

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)

        # 阅读量 +1
        post.increase_views()

        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc'
                                      ])
    except Exception:
        raise Http404

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇post下的全部评论
    comment_list = post.comment_set.all()

    # 将文章，表单，以及文章下的评论列表作为模板传给detail.html模板，以便渲染相应数据
    context = {"post": post,
               "form": form,
               'comment_list': comment_list}
    return render(request, 'blog/detail.html', context=context)


# 通过条件获取归档的博客
def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, 'blog/index.html', context={
        "post_list": post_list
    })


def category(request, id):
    post_list = Post.objects.filter(category__id=id).order_by('-create_time')
    return render(request, 'blog/index.html', context={
        "post_list": post_list
    })
