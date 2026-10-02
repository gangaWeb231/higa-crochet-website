from django.contrib import admin
from .models import Order, Product, Cart, CustomOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "first_name",
        "last_name",
        "phone",
        "product",
        "price",
        "quantity",
        "total_amount",
        "created_at",
    )

    list_filter = (
        "created_at",
        "user",
    )

    search_fields = (
        "first_name",
        "last_name",
        "phone",
        "product",
        "user__username",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "price",
        "category",
        "available",
    )

    list_filter = (
        "category",
        "available",
    )

    search_fields = (
        "name",
        "category",
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "product",
        "price",
        "quantity",
        "created_at",
    )

    search_fields = (
        "product",
        "user__username",
    )

    ordering = (
        "-created_at",
    )


@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "name",
        "phone",
        "item",
        "color",
        "size",
        "quantity",
        "created_at",
    )

    list_filter = (
        "created_at",
        "user",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "item",
        "user__username",
    )

    ordering = (
        "-created_at",
    )