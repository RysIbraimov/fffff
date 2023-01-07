from  rest_framework.permissions import  BasePermission,SAFE_METHODS,IsAdminUser

class IsSenderOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.user.profile.is_sender)
        return bool(request.method in SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        #return bool(request.user and request.user.profile.is_sender)

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and obj.profile == request.user.profile)

class IsBuyerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.profile.is_sender == False)