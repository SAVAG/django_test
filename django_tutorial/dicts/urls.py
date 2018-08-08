from django.urls import path, include
from rest_framework import routers

from django_tutorial.dicts import views


router = routers.DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'genders', views.GenderViewSet)
router.register(r'interest', views.InterestViewSet)

urlpatterns = (
    path('', include(router.urls)),
)
