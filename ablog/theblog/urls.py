from django.urls import path
from .views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, \
    CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', DetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
]
