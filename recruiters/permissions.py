from rest_framework.permissions import BasePermission


class IsRecruiter(BasePermission):
    message = "Only recruiters can access this endpoint."

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return user.role in ["EMPLOYER", "RECRUITER"]