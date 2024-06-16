from rest_framework import serializers
from comment.models import Comment, SubComment


class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 4},
        }


class CommentSerializer(serializers.ModelSerializer):
    subcomments = SubCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 4},
        }
