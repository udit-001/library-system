from rest_framework import generics, status
from rest_framework.response import Response

from .models import *
from .serializers import *


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCheckout(generics.GenericAPIView):
    serializer_class = BookCheckoutSerializer
    queryset = Checkout.objects.all()

    def post(self, *args, **kwargs):
        data = self.request.data
        book_id = kwargs['pk']
        book_obj = generics.get_object_or_404(Book.objects.filter(id=book_id))
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            checked_out_query = Checkout.objects.filter(book=book_obj, return_date__isnull=True)
            if book_obj.num_of_copies > checked_out_query.count():
                obj = serializer.save(book=book_obj)
                response_data = self.serializer_class(obj).data
                return Response(response_data, status.HTTP_200_OK)
            else:
                obj, _ = Reservation.objects.get_or_create(book=book_obj, member=validated_data['member'], reservation_date=validated_data['checkout_date'])
                response_data = BookReserveSerializer(obj).data
                return Response(response_data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookReturn(generics.GenericAPIView):
    serializer_class = BookReturnSerializer
    queryset = Checkout.objects.all()

    def post(self, *args, **kwargs):
        data = self.request.data
        book_id = kwargs['pk']
        book_obj = generics.get_object_or_404(Book.objects.filter(id=book_id))
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            checked_out_query = Checkout.objects.filter(member=validated_data['member'], book=book_obj, return_date__isnull=False)
            if checked_out_query.exists():
                checkout_obj = checked_out_query.first()
                checkout_obj.return_date = validated_data['return_date']
                checkout_obj.save()
                pending_reserve_query = Reservation.objects.filter(book=book_obj, fulfilment_date=validated_data['return_date']).order_by('reservation_date')
                if pending_reserve_query.exists():
                    pending_reserve_obj = pending_reserve_query.first()
                    pending_reserve_obj.fulfillment_date = validated_data['return_date']
                    pending_reserve_obj.save()
                response_data = self.serializer_class(checkout_obj).data
                return Response(response_data, status.HTTP_200_OK)
            else:
                return Response({"detail": "Book wasn't checked out previously"}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
