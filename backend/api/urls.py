from django.urls import path
from .views import decompose_word

# list to define the valid API endpoints
# maps the url for the endpoint to a function
urlpatterns = [
    path('decompose/', decompose_word),
]
