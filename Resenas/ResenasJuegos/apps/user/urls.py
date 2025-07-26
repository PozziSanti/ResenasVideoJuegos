from django.urls import path
from apps.user.views import (
    DashboardView,
    UserSignupView,
    UserLoginView,
)
from blog.views import IndexView
from .views import logout_view
from .views import edit_profile


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='signin'),
    path('logout/', logout_view, name='logout'),
    path('profile/', edit_profile, name='edit_profile'),
]