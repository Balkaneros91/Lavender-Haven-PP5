from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,
            },
        )
