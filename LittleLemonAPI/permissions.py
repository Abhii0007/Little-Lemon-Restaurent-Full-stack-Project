from rest_framework import permissions

class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow users in the 'Manager' group to edit or delete orders.
    """
    def has_permission(self, request, view):
        # Check if the user is in the 'Manager' group
        return request.user.groups.filter(name='Manager').exists()

    def has_object_permission(self, request, view, obj):
        # Check if the user is in the 'Manager' group for the specific object
        return request.user.groups.filter(name='Manager').exists()
