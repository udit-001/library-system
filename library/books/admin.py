from django.contrib import admin
from .models import *


@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ["name", "num_of_copies"]
