from django.db import models
from datetime import date


class Member(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    num_of_copies = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Reservation(models.Model):
    member = models.ForeignKey("books.Member", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    reservation_date = models.DateField()
    fulfillment_date = models.DateField()


class Checkout(models.Model):
    member = models.ForeignKey("books.Member", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    checkout_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField()
