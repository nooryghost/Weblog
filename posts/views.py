from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "posts_create"
    fields = ("title", "slug", "description", "status", "publish")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-publish")
    template_name = "post_list.html"

class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "post_detail.html"

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ("title", "slug", "description")
    success_url = reverse_lazy("posts_list")

    def test_func(self):
        obj = self.get_object
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("posts_list")

    def test_func(self):
        obj = self.get_object
        return obj.author == self.request.user