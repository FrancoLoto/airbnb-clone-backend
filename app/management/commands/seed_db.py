from typing import Any

from app.models import (Amenity, AmenityType, Booking, Photo, Property,
                        PropertyType, Review, Room, RoomBooking, User)
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **options):
        # Deleting all existing data
        User.objects.all().delete()
        AmenityType.objects.all().delete()
        PropertyType.objects.all().delete()
        Room.objects.all().delete()
        Photo.objects.all().delete()
        Property.objects.all().delete()
        Amenity.objects.all().delete()
        Booking.objects.all().delete()
        RoomBooking.objects.all().delete()
        Review.objects.all().delete()

        # Adding new Users
        user1 = User.objects.create_user(
            username='user1', password='password123', is_host=True)
        user2 = User.objects.create_user(
            username='user2', password='password123', is_host=True)
        user3 = User.objects.create_user(
            username='guest1', password='password123', is_host=False)

        # Adding AmenityTypes
        amenity_type1 = AmenityType.objects.create(name='Wi-Fi')
        amenity_type2 = AmenityType.objects.create(name='Aire Acondicionado')
        amenity_type3 = AmenityType.objects.create(name='Bar')
        amenity_type4 = AmenityType.objects.create(name='Gym')

        # Adding PropertyTypes
        property_type1 = PropertyType.objects.create(name='Habitación')
        property_type2 = PropertyType.objects.create(name='Departamento')
        property_type3 = PropertyType.objects.create(name='Casa')

        # Adding Room
        room1 = Room.objects.create(name='Habitación principal', capacity=2)
        room2 = Room.objects.create(name='Habitación invitados', capacity=1)
        room3 = Room.objects.create(name='Living', capacity=4)
        room4 = Room.objects.create(name='Cocina', capacity=1)

        # Adding Photos
        photo1 = Photo.objects.create(
            url='https://a0.muscache.com/im/pictures/miso/Hosting-46641377/original/c1a05bdf-e375-4341-b68a-9046867baf42.jpeg?im_w=720', alt_text='Photo 1')
        photo2 = Photo.objects.create(
            url='https://a0.muscache.com/im/pictures/e23be1e3-0006-428a-819c-cc29e9d1b57a.jpg?im_w=720', alt_text='Photo 2')
        photo3 = Photo.objects.create(
            url='https://a0.muscache.com/im/pictures/hosting/Hosting-1014897621571859054/original/af6cb321-65f2-4578-aae6-efd79323acaa.jpeg?im_w=720', alt_text='Photo 3')
        photo4 = Photo.objects.create(
            url='https://a0.muscache.com/im/pictures/miso/Hosting-967832273777484742/original/524a143d-1d21-4bea-9054-3ce498b235bc.jpeg?im_w=720', alt_text='Photo 4')

        # Adding Properties
        property1 = Property.objects.create(
            host=user1,
            title='Hermosa habitación en el campo',
            description='Una hermosa habitación con baño y Wi-Fi',
            price=110.00,
            location='General Conesa, Argentina',
            available_start=timezone.now(),
            available_end=timezone.now() + timezone.timedelta(days=90),
            property_type=property_type1,
        )
        property1.photos.add(photo1)
        property1.rooms.add(room1, room2, room3)

        property2 = Property.objects.create(
            host=user2,
            title='Moderno departamento en la ciudad',
            description='Un moderno departamento con gimnasio y Wi-Fi',
            price=75.00,
            location='Bahía Blanca, Argentina',
            available_start=timezone.now(),
            available_end=timezone.now() + timezone.timedelta(days=60),
            property_type=property_type2,
        )
        property2.photos.add(photo2)
        property2.rooms.add(room1, room4)

        property3 = Property.objects.create(
            host=user2,
            title="Departamento completo en el centro",
            description="Moderno departamento completo con piscina y dos habitaciones",
            price=154.00,
            location='Las Grutas, Argentina',
            available_start=timezone.now(),
            available_end=timezone.now() + timezone.timedelta(days=80),
            property_type=property_type2,
        )
        property3.photos.add(photo3)
        property3.rooms.add(room1, room3, room4)

        property4 = Property.objects.create(
            host=user1,
            title="Casa moderna completa",
            description="Casa de tres ambientes con Wi-Fi y aire acondicionado",
            price=128.00,
            location='Colonia, Uruguay',
            available_start=timezone.now(),
            available_end=timezone.now() + timezone.timedelta(days=25),
            property_type=property_type3,
        )
        property4.photos.add(photo4)
        property4.rooms.add(room1, room2, room3, room4)

        # Adding Amenities to Properties
        amenity1 = Amenity.objects.create(
            property=property1, amenity_type=amenity_type1)
        amenity2 = Amenity.objects.create(
            property=property1, amenity_type=amenity_type2)
        amenity3 = Amenity.objects.create(
            property=property1, amenity_type=amenity_type3)
        amenity4 = Amenity.objects.create(
            property=property2, amenity_type=amenity_type1)
        amenity5 = Amenity.objects.create(
            property=property2, amenity_type=amenity_type4)

        # Adding Bookings
        booking1 = Booking.objects.create(
            guest=user3,
            property=property1,
            check_in_date=timezone.now() + timezone.timedelta(days=7),
            check_out_date=timezone.now() + timezone.timedelta(days=14),
        )
        booking2 = Booking.objects.create(
            guest=user3,
            property=property2,
            check_in_date=timezone.now() + timezone.timedelta(days=15),
            check_out_date=timezone.now() + timezone.timedelta(days=22),
        )

        # Adding RoomBookings
        room_booking1 = RoomBooking.objects.create(
            room=room1,
            booking=booking1,
            adults=2,
            children=0,
        )
        room_booking2 = RoomBooking.objects.create(
            room=room2,
            booking=booking2,
            adults=1,
            children=0,
        )

        # Adding Reviews
        review1 = Review.objects.create(
            reviewer=user3,
            property=property1,
            review_text='Excelente estadía! El campo estaba hermoso y la recepción fue maravillosa.',
            rating=5,
        )
        review2 = Review.objects.create(
            reviewer=user3,
            property=property2,
            review_text='Gran departamento! Muy moderno y limpio.',
            rating=4,
        )
