from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "num_of_copies"]


class BookReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["member", "reservation_date", ]


class BookCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ["member", "checkout_date", ]


class MemberSerializer(serializers.ModelSerializer):
    reserved_books = BookReserveSerializer(many=True)
    checked_out_books = BookCheckoutSerializer(many=True)
    class Meta:
        model = Book
        fields = ["id", "name", "reserved_books", "checked_out_books"]


class BookReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ["member", "return_date", ]
