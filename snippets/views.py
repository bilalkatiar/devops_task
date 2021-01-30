from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserCreateSerializer
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly, IsSelfOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides List and CRUD actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    @action(detail=True, )
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    This View will automatically provide `List` and `Details` of Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ('post', 'create'):
            return UserCreateSerializer
        return UserSerializer

    def get_permission_classes(self):
        if self.action in ('post', 'create'):
            return permissions.AllowAny
        else:
            return (permissions.IsAuthenticatedOrReadOnly, IsSelfOrReadOnly)
