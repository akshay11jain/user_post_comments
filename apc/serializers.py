from .models import User,Post,Comments
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = User
        fields = ('userId','name' , 'token')
        
class PostSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('post_Id','user' , 'post_title' , 'post_description' )

class CommentsSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Comments
        fields = ('comment_Id','post' , 'comment')
