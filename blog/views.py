from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.
def post_list(request):
    page_number = request.GET.get('page', 1)
    page_list_query = Post.objects.filter(status=Post.Status.PUBLISHED)
    paginator = Paginator(page_list_query, per_page=3)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post/detail.html', {'post': post})
