from django.urls import path
from apps.user.views import UserSignupView, UserLoginView
from blog.views import IndexView
from .views import logout_view, edit_profile, change_password, profile

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='signin'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='user_profile'),
    path('change_password', change_password, name='change_password'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]