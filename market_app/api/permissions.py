from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsStaffOrReadOnly(BasePermission):

    # Überschreibt die Methode `has_permission` von BasePermission
    def has_permission(self, request, view):
        is_flo = request.user and request.user.username == "Flo"

        # Schreibzugriff verweigern, wenn der Nutzer "Flo" ist
        if is_flo and request.method not in SAFE_METHODS:
            return False
        
        is_staff = bool(request.user and request.user.is_staff)
        return is_staff or request.method in SAFE_METHODS