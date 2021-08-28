from rest_framework import permissions


class IsUserOwnerOrGetAndPost(permissions.BasePermission):
    """
        custom permission for actuall UserViewSet to only allow users to edit their own profile, Otherwise User use request Get and Post Only.
    """

    # 'has_permission' function is only use for Get or Post request by User.
    def has_permission(self, request, view):
        return True

    # If you want permission for particalar request like PUT, bcoz data  is already on server so we use this function.
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # change there own data only not others that case for that
        '''
            perfrom edit user by there own data, not other user data
        '''
        if not request.user.is_anonymous:
            return request.user == obj
        
        return False