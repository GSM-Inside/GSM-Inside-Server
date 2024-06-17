from django.urls import path
from .views import *

urlpatterns = [
    path('', CommentView.as_view()),
    path('<int:pk>/', CommentView.as_view()),

    path('sub/', SubCommentView.as_view()),
    path('sub/<int:pk>/', SubCommentView.as_view()),
]
