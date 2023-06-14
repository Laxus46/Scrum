from rest_framework.permissions import BasePermission
class IsSuperUser(BasePermission):
    def has_permission(self, request):
        return request.user.is_superuser
    
class ScrumMaster(BasePermission):
    def has_permission(self, request):
        print(request.user.id)
        return True

class IsAuthenticated(BasePermission):
    def has_permission(self, request):
        return bool(request.user)