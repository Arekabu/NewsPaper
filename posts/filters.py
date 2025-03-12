import django_filters
from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'author__user__username': ['icontains'],
           'date': ['gt'],
       }