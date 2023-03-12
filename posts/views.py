from django.views import generic
from django.urls import reverse_lazy

from .models import Post

class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_time")
    template_name = "post/index.html"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post/post_detail.html"

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy("")

