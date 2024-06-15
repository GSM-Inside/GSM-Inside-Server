from django.urls import path
from .views import *

urlpatterns = [
    path('', GalleryView.as_view()),
    path('request/', GalleryRequestView.as_view())
]