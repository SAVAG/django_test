from rest_framework.permissions import BasePermission


class IsAdminOrIsSelf(BasePermission):

    """
    Allows access only to admin users or an owner.
    """

    def has_permission(self, request, view):
        if request.user:
            if request.user.is_staff:
                return True
            else:
                v = view
        return False
