from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permite el acceso de solo lectura a los usuarios que no son el propietario
    del objeto. Para los usuarios propietarios, se les permite realizar
    operaciones de escritura además de lectura.
    """

    def has_object_permission(self, request, view, obj):
        """
        Verifica si el usuario tiene permiso para realizar una
        acción sobre el objeto.

        Returns:
        - bool: True si el usuario tiene permiso para la acción,
        False de lo contrario.
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.host == request.user
