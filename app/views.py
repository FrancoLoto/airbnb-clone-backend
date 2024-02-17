from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Property
from .permissions import IsOwnerOrReadOnly
from .serializers import BookingSerializer, PropertySerializer


class PropertyListCreateView(generics.ListCreateAPIView):
    """
    Vista de lista y creación para la clase Property.

    Permite a los usuarios listar todas las propiedades
    y crear nuevas propiedades.
    """

    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        """
        Método para guardar la propiedad creada
        con el usuario actual como anfitrión.
        """
        serializer.save(host=self.request.user)


class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista de detalle, actualización y eliminación para la entidad Property.

    Permite a los usuarios ver, actualizar y eliminar propiedades específicas.
    """

    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class BookingListCreateView(generics.ListCreateAPIView):
    """
    Vista de lista y creación para la entidad Booking.

    Permite a los usuarios listar todas las reservas y crear nuevas reservas.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Método para obtener las reservas del usuario actual.
        """

        return Booking.objects.filter(guest=self.request.user)

    def perform_create(self, serializer):
        """
        Método para guardar la reserva creada con el usuario
        actual como huésped.
        """

        serializer.save(host=self.request.user)


class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista de detalle, actualización y eliminación para la entidad Booking.

    Permite a los usuarios ver, actualizar y eliminar reservas específicas.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
