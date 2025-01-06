from django.urls import path
from .views import decompose_word

urlpatterns = [
    path('decompose/', decompose_word),
]
