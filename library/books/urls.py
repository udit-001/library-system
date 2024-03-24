from django.urls import path

from .views import *

urlpatterns = [
    path("books/", BookList.as_view()),
    path("books/<int:pk>/", BookDetail.as_view()),
    path("members/", MemberList.as_view()),
    path("members/<int:pk>/", MemberDetail.as_view()),
]
