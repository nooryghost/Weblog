from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin

from .models import Post, Comment
from .forms import CommentForm

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ("title", "slug", "description", "publish")
    context_object_name = "posts"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostListView(generic.ListView):
    queryset = Post.objects.filter(status="PB").order_by("-publish")
    template_name = "post_list.html"
    context_object_name = "posts"

class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_contex_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()

        return context

class CommentGet(generic.DetailView):
    model = Comment
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()

        return context

class CommentPost(generic.FormView, SingleObjectMixin):
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user

        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()    

        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail.html", kwargs={"pk": post.pk})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ("title", "slug", "description")
    success_url = reverse_lazy("posts_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("posts_list")
    

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
