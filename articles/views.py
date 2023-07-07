from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Article, Category
from .forms import ArticleForm


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
        'no_image': 'https://lavender-haven-pp5.s3.eu-north-1.amazonaws.com/static/media/noimage.png'
    }

    return render(request, 'articles/articles.html', context)


def article_detail(request, article_id):
    """ A view to display the article more detailed view """

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
        'no_image': 'https://lavender-haven-pp5.s3.eu-north-1.amazonaws.com/static/media/noimage.png'
    }

    return render(request, 'articles/article_details.html', context)


@login_required
def add_article(request):
    """ A view for add article to the webshop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(request, 'Successfully added article!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(
                request, 'Failed to add article. Please ensure the form is valid.')
    else:
        form = ArticleForm()

    template = 'articles/add_article.html'

    context = {
        'form': form,
    }

    return render(request, 'articles/add_article.html', context)


@login_required
def edit_article(request, article_id):
    """ Edit a article """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article successfully updated!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(
                request, 'Failed to update article. Please ensure the form is valid.')
    else:
        form = ArticleForm(instance=article)
        messages.info(request, f'You are updating {article.name}')

    template = 'articles/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }

    return render(request, template, context)


@login_required
def delete_article(request, article_id):
    """ Delete a article """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    messages.info(request, 'You are now on the article deletion page.')

    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted!')
        return redirect(reverse('articles'))

    context = {
        'article': article
    }

    return render(request, 'articles/delete_article.html', context)
