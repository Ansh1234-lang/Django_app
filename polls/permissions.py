from rest_framework import permissions # type: ignore

class IsOwnerOrReadOnly(permissions, BaseException):
    """
    custom permission to only allow owner of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # read permission are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permission are only allowed to the owner
        return obj.owner == request.user