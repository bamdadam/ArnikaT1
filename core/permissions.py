from rest_framework import permissions

from core.models import Company

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsCompanyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            company = view.kwargs.get('Company')
            if company:
                Company.objects.get(id=company, admins=request.user.id)
            else:
                Company.objects.get(id=request.data.get('Company'), admins=request.user.id)
            return True
        except Company.DoesNotExist:
            return False
