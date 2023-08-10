from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from taggit.models import Tag

from blog.forms import EmailPostForm, CommentForm
from blog.models import Post


# Create your views here.
def post_list(request, tag_slug=None):
    page_number = request.GET.get('page', 1)
    page_list_query = Post.objects.filter(status=Post.Status.PUBLISHED)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        page_list_query = page_list_query.filter(tags__in=[tag])

    paginator = Paginator(page_list_query, per_page=3)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, post_id):
    queryset = Post.objects.prefetch_related('products')
    post = get_object_or_404(queryset, id=post_id)
    form = CommentForm()
    comments = post.comments.filter(active=True)
    return render(request, 'blog/post/detail.html', {'post': post, 'form': form, 'comments': comments})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{data['name']} 님이 {post.title}을(를) 추천합니다."
            message = f"{post.title}을 {post_url}에서 읽어보세요.\n\n" \
                      f"{data['name']}님의 의견: {data['comments']}"
            send_mail(subject, message, 'jungman82@gmail.com', [data['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(post)
    comments = post.comments.filter(active=True)
    return render(request, 'blog/post/detail.html', {'post': post, 'form': form, 'comments': comments})
