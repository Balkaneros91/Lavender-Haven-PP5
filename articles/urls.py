from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='articles'),
    path('<article_id>', views.article_detail, name='article_detail'),
]
