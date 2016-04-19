from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list,})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post,})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form,
        })

def post_edit(request, pk):
    pass
