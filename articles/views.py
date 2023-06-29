from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
    """ A view to display the article list """

    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)


def article_detail(request, article_id):
    """ A view to display the article more detailed view """

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'articles/article_details.html', context)
