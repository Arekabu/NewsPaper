from tkinter.font import names

from django.urls import path
from .views import PostsList, PostDetail, PostSearch, PostCreate

urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('search', PostSearch.as_view()),
   path('create', PostCreate.as_view()),
]