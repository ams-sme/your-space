from django.shortcuts import render,redirect
from django.views.generic import DetailView
from feed.forms import PostForm
from .models import Post, Comment

def home(request):
    posts = Post.objects.all().order_by('-created_date')
    context = {'posts': posts}
    return render(request, 'feed/home.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed:home')  # Adjust the URL name as per your setup
    else:
        form = PostForm()
    
    return redirect('feed:home')


class PostDetailView(DetailView):
    model = Post
    template_name = 'feed/post_detail.html'
    context_object_name = 'post'
    
def comment_create(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        content = request.POST['content']
        Comment.objects.create(post=post, user=request.user, content=content)
    return redirect('feed:post_detail', pk=pk)