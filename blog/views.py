from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import viewsets
from . import models
from rest_framework import viewsets, permissions
from . import models, serializers
from rest_framework import filters, pagination
# Create your views here.


class BlogPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100



class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    pagination_class = BlogPagination
    search_fields = ['user__username','topic','title']

    def create(self, request, *args, **kwargs):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)
        # If user is authenticated, proceed with creating the blog
        return super().create(request, *args, **kwargs)



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.none()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)
        return super().create(request, *args, **kwargs)
