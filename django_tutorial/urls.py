"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

from django_tutorial import settings
from django_tutorial.accounts import views as accounts_views

router = routers.DefaultRouter()
router.register(r'users', accounts_views.UserViewSet)
router.register(r'profiles', accounts_views.ProfileViewSet)
router.register(r'groups', accounts_views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    re_path('dictionaries/?', include('django_tutorial.dicts.urls')),
    path(
        'docs/',
        include_docs_urls(
            title='My Django tutorial docs',
            authentication_classes=[],
            permission_classes=[settings.REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']],
            public=True
        ),
    ),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
