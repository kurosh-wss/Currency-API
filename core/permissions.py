from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    message = "You do not have permission to this object."

    def has_object_permission(self, request, view):
        if request.user.groups.filter(name="Customer").exists():
            return True
        return False
