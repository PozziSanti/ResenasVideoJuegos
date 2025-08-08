from django.urls import path
<<<<<<< HEAD
from apps.post.views import (PostCategoryFilter, PostTitleFilter, PostDateFilter, PostStarFilter,)

urlpatterns = [
    path('search/', PostTitleFilter.as_view(), name='post_search'),
    path('category/<str:category>/', PostCategoryFilter.as_view(), name='post_by_category'),
    path('date/', PostDateFilter.as_view(), name='post_by_date'), 
    path('star/', PostStarFilter.as_view(), name='post_by_star'),
]
=======
from apps.post.views import IndexView, AboutView, TermsView, PrivacyPolicyView, PostDetailView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),  # Sobre nosotros 
    path('terms/', TermsView.as_view(), name='terms'),  # Terminos y condiciones 
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),  # Politica de Privacidad
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
>>>>>>> 6a9c813d0b41b2a973109fec29edd18ac976fa90
