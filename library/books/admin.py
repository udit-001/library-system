from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import *


@admin.register(Member)
class Member(ImportExportMixin, admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["created_at"]


class CheckoutInline(admin.TabularInline):
    model = Checkout
    extra = 1
    readonly_fields = ["due_date"]


class ReservationInline(admin.TabularInline):
    model = Checkout
    extra = 1
    readonly_fields = ["due_date"]


@admin.register(Book)
class Book(ImportExportMixin, admin.ModelAdmin):
    list_display = ["name", "num_of_copies"]
    search_fields = ["name"]
    list_filter = ["created_at"]
    inlines = [CheckoutInline, ReservationInline]
