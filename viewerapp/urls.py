from django.urls import path
from viewerapp.views import SearchCommentByPost, AddComment

urlpatterns = [
    path('search/',SearchCommentByPost.as_view() ),
    path('add/comment/',AddComment.as_view() )
]
