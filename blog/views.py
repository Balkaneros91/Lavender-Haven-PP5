from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Blog


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6


class BlogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = {
            "blog": blog,
            "liked": liked,
        }
        if not request.user.is_authenticated:
            messages.info(request, "You need to be logged in to like a blog.")

        return render(request, "blog/blog_detail.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = {
            "blog": blog,
            "liked": liked,
        }
        if not request.user.is_authenticated:
            messages.info(request, "You need to be logged in to like a blog.")

        return render(request, "blog/blog_detail.html", context)


class BlogLike(View):
    """ View for liking the post if user is authenticated """
    def post(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)

        if blog.likes.filter(id=self.request.user.id).exists():
            blog.likes.remove(request.user)
            messages.info(request, "You have unliked the blog.")
        else:
            blog.likes.add(request.user)
            messages.info(request, "You have liked the blog.")

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))
