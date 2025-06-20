"""
URL configuration for NewsPaper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from posts.views import Index, PostsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostsList.as_view()),
    path('news/', include('posts.urls')),
    path('articles/', include('posts.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('protect.urls')),
    path('index/', Index.as_view(), name='post_index'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
