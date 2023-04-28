from django.urls import path
from blog.views import post_index

urlpatterns = [
    path('', post_index),
]
