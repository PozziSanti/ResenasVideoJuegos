from django.urls import path
from apps.post.views import (IndexView, AboutView, TermsView, PrivacyPolicyView,
                            PostListView, PostUpdateView, PostDeleteView, PostCreateView, PostDetailView, 
                            PostCategoryFilter, PostTitleFilter, PostDateFilter, PostStarFilter, PostAutocomplete)


urlpatterns = [
    path('home/', IndexView.as_view(), name='home'), # Pagina principal
    path('about/', AboutView.as_view(), name='about'),  # Sobre nosotros 
    path('terms/', TermsView.as_view(), name='terms'),  # Terminos y condiciones 
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),  # Politica de Privacidad
    path('post/', PostListView.as_view(), name='post_list'),
    path('search/', PostTitleFilter.as_view(), name='post_search'),
    path('autocomplete/', PostAutocomplete.as_view(), name='post_autocomplete'),
    path('category/<str:category>/', PostCategoryFilter.as_view(), name='post_by_category'),
    path('date/', PostDateFilter.as_view(), name='post_by_date'), 
    path('star/', PostStarFilter.as_view(), name='post_by_star'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
]
