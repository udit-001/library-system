from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "num_of_copies"]


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name"]


class BookEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookEvent
        fields = ["id", "member", "book", "event_type"]
