from django.urls import path
from apps.post.views import (PostCategoryFilter, PostTitleFilter, PostDateFilter, PostStarFilter,)

urlpatterns = [
    path('search/', PostTitleFilter.as_view(), name='post_search'),
    path('category/<str:category>/', PostCategoryFilter.as_view(), name='post_by_category'),
    path('date/', PostDateFilter.as_view(), name='post_by_date'), 
    path('star/', PostStarFilter.as_view(), name='post_by_star'),
]