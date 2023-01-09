from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.profile.is_sender)
        return bool(
            request.method in SAFE_METHODS or
            request.user.profile.is_sender
        )

class IsNotAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.profile.is_sender)
        return bool(
            request.method in SAFE_METHODS or
            request.user.profile.is_sender is False
        )

