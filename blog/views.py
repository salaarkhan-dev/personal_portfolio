from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator


# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')

    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
