from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Article


def article_list(request):
    """ A view to display the article list """

    articles = Article.objects.all()
    query = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")  # noqa
                return redirect(reverse('articles'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            articles = articles.filter(queries)

    context = {
        'articles': articles,
        'search_term': query,
    }

    return render(request, 'articles/articles.html', context)


def article_detail(request, article_id):
    """ A view to display the article more detailed view """

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'articles/article_details.html', context)
