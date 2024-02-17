from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import (Amenity, AmenityType, Booking, Photo, Property,
                     PropertyType, Review, Room, RoomBooking, User)


class CustomRegisterSerializer(RegisterSerializer):
    """
    Serializador personalizado para el registro de usuarios.

    Agrega un campo adicional 'is_host' que indica si el
    usuario es un anfitrión.
    """

    is_host = serializers.BooleanField(required=False)

    def get_cleaned_data(self):
        """
        Obtiene los datos limpios del formulario de registro.

        Returns:
        - dict: Diccionario con los datos limpios.
        """

        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'is_host': self.validated_data.get('is_host', ''),
        }


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User.
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_host',)


class RoomSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Room.
    """

    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Booking.
    """

    class Meta:
        model = Booking
        fields = '__all__'


class RoomBookingSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo RoomBooking.
    """

    class Meta:
        model = RoomBooking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Review.
    """

    class Meta:
        model = Review
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Photo.
    """

    class Meta:
        model = Photo
        fields = '__all__'


class PropertyTypeSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo PropertyType.
    """

    class Meta:
        model = PropertyType
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Amenity.
    """

    class Meta:
        model = Amenity
        fields = '__all__'


class AmenityTypeSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo AmenityType.
    """

    class Meta:
        model = AmenityType,
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Property.

    Incluye el serializador anidado UserSerializer para el campo 'host'.
    """

    host = UserSerializer()

    class Meta:
        model = Property
        fields = '__all__'
        depth = 1
