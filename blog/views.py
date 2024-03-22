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
    page_size = 2
    page_size_query_param = page_size
    max_page_size = 100


class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = BlogPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username','user__id','topic','title']

    def create(self, request, *args, **kwargs):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)
        # Set the user for the blog post before saving
        request.data['user'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Check if the requesting user is the creator of the blog
        if request.user == instance.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "You don't have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['blog__id']

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)
        return super().create(request, *args, **kwargs)
