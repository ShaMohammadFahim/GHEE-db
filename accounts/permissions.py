from rest_framework import permissions

class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
       
        return (request.user.is_authenticated and 
                request.user.role and 
                request.user.role.name == 'Admin')

class IsCustomerRole(permissions.BasePermission):
    def has_permission(self, request, view):
     
        return (request.user.is_authenticated and 
                request.user.role and 
                request.user.role.name == 'Customer')