from rest_framework import permissions

from core.models import Company


class IsCompanyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            Company.objects.get(id=view.kwargs.get('Company'), admins=request.user.id)
            return True
        except Company.DoesNotExist:
            return False
