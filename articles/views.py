from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Article, Category


def article_list(request):
    """ A view to display the article list """

    articles = Article.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                articles = articles.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            articles = articles.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            articles = articles.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")  # noqa
                return redirect(reverse('articles'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            articles = articles.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'articles': articles,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'articles/articles.html', context)


def article_detail(request, article_id):
    """ A view to display the article more detailed view """

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'articles/article_details.html', context)
