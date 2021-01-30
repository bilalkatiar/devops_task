from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight',
        format='html'
    )

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        view_name='snippet-detail',
        many=True,
        read_only=True
    )
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'date_joined',
                  'snippets')


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_staff',
                  'date_joined')

    def create(self, validated_data):
        password = validated_data.get('password')

        user = super(UserCreateSerializer, self).create(validated_data)

        user.set_password(password)
        user.save()
        return user
