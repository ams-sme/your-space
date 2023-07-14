from django.urls import path

from user_profile.views import (ProfileDetailView, ProfileUpdateView,
                                login_view, logout_view, registration_view)

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<slug:slug>/', ProfileDetailView.as_view(), name='detail'),
    path('<slug:slug>/edit/', ProfileUpdateView.as_view(), name='update'),
]
