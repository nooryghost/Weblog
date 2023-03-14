from django.urls import path

from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("create/", PostCreateView.as_view(), name="posts_create"),
    path("list/", PostListView.as_view(), name="posts_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="posts_detail"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="posts_edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="posts_delete")
]