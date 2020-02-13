from django.urls import path

from . import views

urlpatterns=[
    path('posts/',views.HomePageView.as_view(), name='posts')
]