from django.urls import path

from .views import \
    BlogListView,\
    BlogDetailView,\
    BlogCreateView,\
    BlogUpdateView,\
    BlogDeleteView, \
    HomePageView

urlpatterns = [
    path('blog/post/new/', BlogCreateView.as_view(), name='post_new'),
    path('blog/post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('blog/post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('blog/post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('', HomePageView.as_view(), name='home')

]