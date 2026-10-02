from django.urls import path
from . import views

urlpatterns = [

    # Home
    path("", views.index, name="index"),

    # Shop
    path("shop/", views.shop, name="shop"),

    # Product Details
    path(
        "product/<int:id>/",
        views.product_details,
        name="product_details"
    ),

    # Cart
    path(
        "cart/",
        views.cart,
        name="cart"
    ),

    path(
        "add-to-cart/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),

    # Custom Order
    path(
        "custom-order/",
        views.custom_order,
        name="custom_order"
    ),

    # Login
    path(
        "login/",
        views.user_login,
        name="login"
    ),

    path(
        "logout/",
        views.user_logout,
        name="logout"
    ),

    # Account
    path(
        "account/",
        views.account,
        name="account"
    ),

    # Orders
    path(
        "orders/",
        views.orders,
        name="orders"
    ),

    path(
        "place-order/",
        views.place_order,
        name="place_order"
    ),
]