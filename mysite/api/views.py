from django.shortcuts import render
from rest_framework import filters, generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [filters.SearchFilter]

    # Enables partial search
    search_fields = ['title']

# Filter & delete
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'

# Bulk delete
class BlogPostBulkDelete(generics.DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        self.get_queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)