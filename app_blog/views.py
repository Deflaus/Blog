from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CreatePost


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'post/list.html'
    queryset = Post.objects.all()[:10]


class PostDetailView(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = 'post/detail.html'


def create_post(request):
    created = False
    new_post = None
    if request.method == 'POST':
        post_form = CreatePost(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.image = request.FILES['image']
            new_post.save()
            created = True
    else:
        post_form = CreatePost()
    return render(request, 'post/createpost.html',
                  {'post_form': post_form, 'created': created, })
