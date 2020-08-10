from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>', views.archives, name='archives'),
    path('category/<int:id>', views.category, name='category')
]