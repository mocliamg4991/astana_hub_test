from rest_framework import permissions

class IsManager(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_manager)

    def has_permission(self, request, view):
        return bool(request.user.is_manager)