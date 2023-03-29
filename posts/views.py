from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

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

class CommentGet(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()

        return context

class CommentPost(SingleObjectMixin, generic.FormView):
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
        return reverse("posts_detail", kwargs={"pk": post.pk})
    
class PostLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
            
        if not is_like:
            post.likes.add(request.user)

        else:
            post.likes.remove(request.user)

        next = request.POST.get("next", "/")
        return HttpResponseRedirect(next)

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        
        return view(request, *args, **kwargs)   
    

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
