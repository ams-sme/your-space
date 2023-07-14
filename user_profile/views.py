from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from user_profile.forms import ProfileForm
from user_profile.models import Profile
from django.views import View
from feed.models import Post

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed:home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('profile:login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('feed:home') 


class ProfileDetailView(View):
    def get(self, request, slug):
        profile = get_object_or_404(Profile, user__username=slug)
        posts = Post.objects.filter(user__username=slug)
        context = {
            'profile': profile,
            'posts': posts,
            'own_profile': request.user == profile.user
        }
        return render(request, 'user_profile/detail.html', context)
    
    
class ProfileUpdateView(View):
    def get(self, request, slug):
        profile = get_object_or_404(Profile, user__username=slug)
        form = ProfileForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'user_profile/update.html', context)

    def post(self, request, slug):
        profile = get_object_or_404(Profile, user__username=slug)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile:detail', slug=slug)
        return render(request, 'user_profile/update.html', {'form': form})
