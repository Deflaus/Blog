from django.urls import path
from .views import PostListView, PostDetailView, create_post


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('createpost/', create_post, name='post_create'),
]
