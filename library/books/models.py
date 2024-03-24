from django.db import models
from django.utils import timezone


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
    member = models.ForeignKey("books.Member", on_delete=models.CASCADE, related_name="reserved_books")
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    reservation_date = models.DateField()
    fulfillment_date = models.DateField(null=True, blank=True)


class Checkout(models.Model):
    member = models.ForeignKey("books.Member", on_delete=models.CASCADE, related_name="checked_out_books")
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    checkout_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.due_date = self.checkout_date + timezone.timedelta(days=7)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.return_date is not None:
            return f"{self.member} checked out {self.book} and returned on {self.return_date}"
        else:
            return f"{self.member} checked out {self.book} and hasn't returned"
