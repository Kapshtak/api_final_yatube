import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        return super().to_internal_value(data)


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
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    following = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Follow
        fields = ("user", "following")


class FollowCreateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    following = serializers.CharField()

    class Meta:
        model = Follow
        fields = (
            "user",
            "following",
        )

    def validate_following_username(self, value):
        try:
            User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "Пользователь с таким username не существует"
            )
        return value

    def create(self, validated_data):
        following = validated_data["following"]
        following_user = User.objects.get(username=following)
        user = self.context["request"].user

        if user == following_user:
            raise serializers.ValidationError(
                "Вы не можете фолловить сами себя"
            )

        follow, created = Follow.objects.get_or_create(
            user=user, following=following_user
        )
        if not created:
            raise serializers.ValidationError(
                "Вы уже следите за этим пользователем"
            )

        return follow
