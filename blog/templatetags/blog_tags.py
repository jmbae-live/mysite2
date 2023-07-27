from django import template
from django.db.models import Count

from blog.models import Post

register = template.Library()


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.filter(status=Post.Status.PUBLISHED) \
               .annotate(total_comments=Count('comments')) \
               .order_by('-total_comments')[:count]
