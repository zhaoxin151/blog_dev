from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    内部类Meta里指定一些和表单相关的东西。model = Comment表明这个数据库模型是Comment类
    fields 指定了表单需要显示的字段
    '''
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
