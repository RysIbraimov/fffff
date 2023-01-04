from  rest_framework.permissions import  BasePermission,SAFE_METHODS,IsAdminUser

class IsSenderOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        if request.methos in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.profile.is_sender)



