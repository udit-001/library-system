from django.db import models


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


class EventType(models.TextChoices):
    CHECKOUT = "checkout", "Checkout"
    RETURN = "return", "Return"
    RESERVE = "reserve", "Reserve"
    FULFILL = "fulfill", "Fulfill"


class BookEvent(models.Model):
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    member = models.ForeignKey("books.Member", on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.event_type} - {self.book}"
