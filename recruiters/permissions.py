from rest_framework.permissions import BasePermission


class IsRecruiter(BasePermission):
    message = "Only recruiters can access this endpoint."

    def has_permission(self, request, view):
        user = request.user

<<<<<<< HEAD
        if not user or not user.is_authenticated:
            return False

        return user.role in ["EMPLOYER", "RECRUITER"]
=======
        return bool(
            user
            and user.is_authenticated
            and user.is_active
            and getattr(user, "role", None) == "RECRUITER"
        )


class HasRecruiterProfile(BasePermission):
    message = "Recruiter profile was not found."

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return hasattr(user, "recruiter_profile")


class IsVerifiedRecruiter(BasePermission):
    message = "Please verify your account before continuing."

    def has_permission(self, request, view):
        user = request.user

        return bool(
            user
            and user.is_authenticated
            and user.is_active
            and getattr(user, "role", None) == "RECRUITER"
        )
>>>>>>> e2ad693 (commit msg)
