from django.urls import path

from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, PostLike

urlpatterns = [
    path("create/", PostCreateView.as_view(), name="posts_create"),
    path("", PostListView.as_view(), name="posts_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="posts_detail"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="posts_edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="posts_delete"),
    path("<int:pk>/like", PostLike.as_view(), name="like") 
]