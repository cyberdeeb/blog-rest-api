from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-update'),
    path('blogposts/delete-all/', views.BlogPostBulkDelete.as_view(), name='blogpost-delete-all')
]