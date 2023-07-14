from django.urls import path
from feed.views import create_post, home, PostDetailView, comment_create

urlpatterns = [
    path('', home, name='home'),
    path('post/create/', create_post, name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', comment_create, name='create_comment'),

]
