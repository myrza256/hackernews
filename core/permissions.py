from rest_framework.permissions import BasePermission


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author.id == request.user.id:
            return True
        else:
            return False
