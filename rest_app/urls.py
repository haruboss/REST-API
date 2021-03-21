from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages',views.indexView)
router.register('paradigms',views.ParadigmsView)
router.register('programmer',views.ProgrammerView)

urlpatterns = [
    path('',include(router.urls) ),
    ]