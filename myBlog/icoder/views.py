from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
    DetailView,
    CreateView, 
    UpdateView,
    DeleteView
) 

posts = Post.objects.all()
# Create your views here.
def home(request):
    context = {'posts':posts}
    return render(request, 'icoder/home.html', context)


# creating a class based view for home page
class Homeview(ListView):
    model = Post
    template_name = 'icoder/home.html'
    context_object_name = 'posts'
    ordering = ['-dateposted']
    paginate_by =1


class UserPostListView(ListView):
    model = Post
    template_name = 'icoder/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-dateposted']
    paginate_by =1

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(user = user).order_by('-dateposted') 


# creating a detail view post for each post
class PostView(DetailView):
    model = Post


class Createpostview(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Updatepostview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model  = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False     


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False     



def about(request):
    return HttpResponse("<h1>About</h1>")


