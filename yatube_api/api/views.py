from django.shortcuts import get_object_or_404
from rest_framework import permissions, mixins, filters, exceptions
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Group, Post, Follow
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from api.pagination import CustomPagination
from api.serializers import PostSerializer

from api.serializers import (CommentSerializer,
                             GroupSerializer,
                             PostSerializer,
                             FollowSerializer)
from api.permissions import IsAuthorOrReadOnly

SUB_TO_SELF = 'Подписка на самого себя!'


class CreateListViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass


class ListRetrieveViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    pass


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    pagination_class = CustomPagination
    filterset_fields = ('text', 'author', 'group', 'pub_date',)
    search_fields = ('text',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(CreateListViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        if self.request.user.username == self.request.data['following']:
            raise exceptions.ValidationError(SUB_TO_SELF)
        serializer.save(user=self.request.user)


class GroupViewSet(ListRetrieveViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_class = (permissions.IsAuthenticated,)
    pagination_class = None


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )
    pagination_class = None

    def get_queryset(self):
        return get_object_or_404(
            Post,
            id=self.kwargs.get('post_id')
        ).comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.kwargs.get('post_id'))
        )
