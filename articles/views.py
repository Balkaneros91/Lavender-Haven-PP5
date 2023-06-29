from django.shortcuts import render
from .models import Article


def article_list(request):
    """ A view to display the article list """

    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)
