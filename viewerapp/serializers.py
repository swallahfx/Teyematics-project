from rest_framework import serializers
from viewerapp.models import Posts, Comments

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['postId', 'name', 'email', 'body']
        
class SearchSerializer(serializers.Serializer):
        search =serializers.CharField()