from rest_framework import generics

from .models import *
from .serializers import *


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class BookEventList(generics.ListCreateAPIView):
    queryset = BookEvent.objects.all()
    serializer_class = BookEventSerializer


class BookEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookEvent.objects.all()
    serializer_class = BookEventSerializer
