from django.urls import path
from apps.post.views import (PostCategoryFilter, PostTitleFilter, PostDateFilter, PostStarFilter, 
                             PostListView, 
                             PostUpdateView,
                             PostDeleteView,
                             PostCreateView, 
                             PostDetailView)
from apps.post.views import IndexView, AboutView, TermsView, PrivacyPolicyView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),
    path('search/', PostTitleFilter.as_view(), name='post_search'),
    path('category/<str:category>/', PostCategoryFilter.as_view(), name='post_by_category'),
    path('date/', PostDateFilter.as_view(), name='post_by_date'), 
    path('star/', PostStarFilter.as_view(), name='post_by_star'),
    path('home/', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),  # Sobre nosotros 
    path('terms/', TermsView.as_view(), name='terms'),  # Terminos y condiciones 
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),  # Politica de Privacidad
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
]
