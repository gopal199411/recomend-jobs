from rest_framework.permissions import BasePermission


# ==========================================
# Allow only authenticated users
# ==========================================

class IsAuthenticatedUser(BasePermission):
    """
    Allow access only for logged-in users
    """

    def has_permission(self, request, view):

        return (
            request.user
            and
            request.user.is_authenticated
        )



# ==========================================
# Allow only Admin users
# ==========================================

class IsAdminUser(BasePermission):
    """
    Allow only admin users to create/update/delete jobs
    """

    def has_permission(self, request, view):

        return (
            request.user
            and
            request.user.is_authenticated
            and
            request.user.is_staff
        )



# ==========================================
# Allow Read Only Access
# ==========================================

class ReadOnlyPermission(BasePermission):
    """
    Anyone can GET data,
    only authenticated users can modify
    """

    def has_permission(self, request, view):

        if request.method in [
            "GET",
            "HEAD",
            "OPTIONS"
        ]:
            return True


        return (
            request.user
            and
            request.user.is_authenticated
        )



# ==========================================
# Candidate Permission
# ==========================================

class IsCandidate(BasePermission):
    """
    Candidate can access recommendation API
    """

    def has_permission(self, request, view):

        return (
            request.user
            and
            request.user.is_authenticated
            and
            getattr(
                request.user,
                "role",
                None
            )
            == "CANDIDATE"
        )



# ==========================================
# Employer Permission
# ==========================================

class IsEmployer(BasePermission):
    """
    Employer can manage job postings
    """

    def has_permission(self, request, view):

        return (
            request.user
            and
            request.user.is_authenticated
            and
            getattr(
                request.user,
                "role",
                None
            )
            == "EMPLOYER"
        )