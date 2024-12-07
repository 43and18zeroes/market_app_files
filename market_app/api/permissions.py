# Importiert die notwendigen Klassen und Konstanten aus Django REST Framework
from rest_framework.permissions import BasePermission, SAFE_METHODS

# Definiert eine benutzerdefinierte Berechtigungsklasse, die von BasePermission erbt
class IsStaffOrReadOnly(BasePermission):
    """
    Berechtigungsklasse, die es nur Staff-Mitgliedern erlaubt,
    schreibende Aktionen auszuführen, während alle anderen
    nur lesende Aktionen durchführen können.
    """

    # Überschreibt die Methode `has_permission` von BasePermission
    def has_permission(self, request, view):
        """
        Überprüft, ob ein Nutzer die Berechtigung hat, auf die angeforderte Ansicht zuzugreifen.

        - Staff-Mitglieder haben Schreib- und Leseberechtigungen.
        - Andere Nutzer haben nur Leseberechtigungen (für sichere HTTP-Methoden wie GET).
        """

        # Überprüft, ob der Nutzer authentifiziert ist und ein Staff-Mitglied ist
        # - `request.user` gibt das Nutzerobjekt zurück.
        # - `request.user.is_staff` ist True, wenn der Nutzer ein Staff-Mitglied ist.
        is_staff = bool(request.user and request.user.is_staff)

        # Gibt True zurück, wenn der Nutzer ein Staff-Mitglied ist
        # ODER wenn die HTTP-Methode in den sicheren Methoden (SAFE_METHODS) enthalten ist
        # - `SAFE_METHODS` umfasst GET, HEAD und OPTIONS, die keine Änderungen an den Ressourcen vornehmen.
        return is_staff or request.method in SAFE_METHODS
