from django.urls import path
from apps.post.views import (PostCategoryFilter, PostTitleFilter, PostDateFilter, PostStarFilter,)
from apps.post.views import IndexView, AboutView, TermsView, PrivacyPolicyView, PostDetailView

urlpatterns = [
    path('search/', PostTitleFilter.as_view(), name='post_search'),
    path('category/<str:category>/', PostCategoryFilter.as_view(), name='post_by_category'),
    path('date/', PostDateFilter.as_view(), name='post_by_date'), 
    path('star/', PostStarFilter.as_view(), name='post_by_star'),
    path('home/', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),  # Sobre nosotros 
    path('terms/', TermsView.as_view(), name='terms'),  # Terminos y condiciones 
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),  # Politica de Privacidad
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
