from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """

    """

    def has_object_permission(self, request, view, obj):
        """
        This method extends the has_object_permission to implement object level permissions

        :param request:
        :param view:
        :param obj:
        :return:
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsSelfOrReadOnly(permissions.BasePermission):
    """

    """

    def has_object_permission(self, request, view, obj):
        """
        This method extends the has_object_permission to implement object level permissions

        :param request:
        :param view:
        :param obj:
        :return:
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user


