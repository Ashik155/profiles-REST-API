from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''allow user to edit thier own profile'''

    def has_object_permission(self,request,view,obj):
        '''allow user to edit only thier profiles'''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.id
    
class UpdateByOnlyThatUser(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        '''allow user to edit only thier profiles'''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.user_profile.id
