from rest_framework import serializers
from .models import Likes

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']