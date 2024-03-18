from rest_framework import serializers
from . import models



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields='__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
