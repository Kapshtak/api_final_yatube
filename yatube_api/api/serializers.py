from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from api.fields import Base64ImageField
from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = ("id", "author", "text", "pub_date", "image", "group")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=Comment.objects.all(),
        slug_field="username",
        read_only=False,
        required=False,
    )

    class Meta:
        fields = "__all__"
        read_only_fields = ("author", "post")
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "slug", "description")
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ("user", "following")
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="Вы уже подписаны на этого пользователя",
            )
        ]

    def validate(self, data):
        user = data["user"]
        following = data["following"]
        if user == following:
            raise serializers.ValidationError(
                "Вы не можете фолловить сами себя"
            )
        try:
            User.objects.get(username=following)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "Пользователь с таким username не существует"
            )

        return data
