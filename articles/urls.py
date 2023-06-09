from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='articles'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:article_id>', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>', views.delete_article, name='delete_article'),
]
