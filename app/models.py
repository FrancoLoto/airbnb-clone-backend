from django.contrib.auth.models import AbstractUser
from django.db import models


# Modelo de Usuario
class User(AbstractUser):
    is_host = models.BooleanField(default=False)


# Este modelo se crea para almacenar diferentes tipos de características de las propiedades
class AmenityType(models.Model):
    name = models.CharField(max_length=100)


# Este modelo se utiliza para almacenar diferentes tipos de propiedades
class PropertyType(models.Model):
    name = models.CharField(max_length=100)


# Este modelo se utiliza para almacenar información sobre habitaciones dentro de propiedades
class Room(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.PositiveSmallIntegerField()


# Este modelo se utiliza para almacenar información detallada sobre una propiedad
class Property(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=200)
    available_start = models.DateField()
    available_end = models.DateField()
    photos = models.ManyToManyField('Photo')
    property_type = models.ForeignKey(
        PropertyType, on_delete=models.SET_NULL, null=True)
    rooms = models.ManyToManyField(Room)
    amenities = models.ManyToManyField(AmenityType, through='Amenity')


# Este modelo se utiliza para vincular características a propiedades
class Amenity(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='property_amenities')
    amenity_type = models.ForeignKey(
        AmenityType,
        on_delete=models.CASCADE,
        default=None,
        related_name='amenity_type')


# Este modelo se utiliza para almacenar información de reservas realizadas por los huéspedes
class Booking(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    rooms = models.ManyToManyField(Room, through='RoomBooking')


# Este modelo se utiliza para almacenar detalles de reservas de habitaciones dentro de una reserva general
class RoomBooking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    adults = models.PositiveSmallIntegerField()
    children = models.PositiveSmallIntegerField()


# Este modelo se utiliza para almacenar reseñas realizadas por usuarios para propiedades
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField()


# Este modelo se utiliza para almacenar información sobre fotos relacionadas con propiedades
class Photo(models.Model):
    url = models.URLField()
    alt_text = models.CharField(max_length=200)
