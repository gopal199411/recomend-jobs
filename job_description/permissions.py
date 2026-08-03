from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS
)



# =====================================================
# Read Only Permission
# =====================================================

class ReadOnlyPermission(BasePermission):
    """
    Allow GET, HEAD, OPTIONS only
    """

    def has_permission(
        self,
        request,
        view
    ):

        return request.method in SAFE_METHODS





# =====================================================
# Job Owner Permission
# =====================================================

class IsJobOwnerOrReadOnly(BasePermission):
    """
    Read access for everyone.
    Modify access only for owner/admin.
    """


    def has_permission(
        self,
        request,
        view
    ):

        # Allow GET, OPTIONS, HEAD

        if request.method in SAFE_METHODS:

            return True


        # For create/update/delete
        # user must be authenticated

        return (
            request.user
            and
            request.user.is_authenticated
        )



    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        # Read access

        if request.method in SAFE_METHODS:

            return True



        # Admin can modify

        if request.user.is_staff:

            return True



        return False





# =====================================================
# Admin Only Permission
# =====================================================

class IsAdminUser(BasePermission):
    """
    Only admin users can modify jobs.
    """


    def has_permission(
        self,
        request,
        view
    ):

        return (

            request.user

            and

            request.user.is_authenticated

            and

            request.user.is_staff

        )