from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
     path("users/logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]