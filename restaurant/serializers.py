from rest_framework import serializers
from .models import Booking, Menu

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # or ['id', 'first_name', 'reservation_date', 'reservation_slot']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # or ['id', 'name', 'price', 'menu_item_description']
