import json
from decimal import Decimal, InvalidOperation

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import JsonResponse

from .models import Order, Cart, CustomOrder


# =========================
# HOME
# =========================
def index(request):
    return render(request, "index.html")


# =========================
# SHOP PAGE
# =========================
def shop(request):
    return render(request, "shop.html")


# =========================
# PRODUCT DETAILS
# =========================
def product_details(request, id):

    products = {

        1: {
            "name": "Bow Frock",
            "image": "app1/images/frock.png",
            "price": 1600,
            "old_price": 1800,
            "rating": "4.8 (25 Reviews)",
            "description": "Beautiful handmade crochet bow frock made using premium soft cotton yarn.",
            "material": "Cotton Yarn",
            "color": "Lavender",
            "size": "0-6 Months",
        },

        2: {
            "name": "Chick Keychain",
            "image": "app1/images/chick.png",
            "price": 399,
            "old_price": 499,
            "rating": "4.9 (18 Reviews)",
            "description": "Cute handmade crochet chick keychain.",
            "material": "Cotton Yarn",
            "color": "Yellow",
            "size": "4 Inches",
        },

        3: {
            "name": "Peony Flower",
            "image": "app1/images/peony.png",
            "price": 299,
            "old_price": 399,
            "rating": "5 (22 Reviews)",
            "description": "Elegant handmade crochet Peony Flower.",
            "material": "Cotton Yarn",
            "color": "Pink",
            "size": "12 Inches",
        },

        4: {
            "name": "Sunflower Bag",
            "image": "app1/images/sunflowerbag.png",
            "price": 1200,
            "old_price": 1500,
            "rating": "4.5 (18 Reviews)",
            "description": "Handmade crochet sunflower shoulder bag.",
            "material": "Cotton Yarn",
            "color": "Yellow",
            "size": "Medium",
        },

        5: {
            "name": "Baby Booties",
            "image": "app1/images/babybootie.png",
            "price": 450,
            "old_price": 550,
            "rating": "4.8 (15 Reviews)",
            "description": "Soft crochet baby booties.",
            "material": "Cotton Yarn",
            "color": "Cream",
            "size": "0-6 Months",
        },

        6: {
            "name": "Cardigan",
            "image": "app1/images/cardigan.png",
            "price": 2200,
            "old_price": 2500,
            "rating": "5 (20 Reviews)",
            "description": "Handmade crochet cardigan.",
            "material": "Cotton Yarn",
            "color": "Beige",
            "size": "S / M / L",
        },

        7: {
            "name": "Daisy Keychain",
            "image": "app1/images/daisy.png",
            "price": 250,
            "old_price": 300,
            "rating": "4.5 (10 Reviews)",
            "description": "Cute daisy crochet keychain.",
            "material": "Cotton Yarn",
            "color": "White",
            "size": "4 Inches",
        },

        8: {
            "name": "Bow Handbag",
            "image": "app1/images/bowbag.png",
            "price": 1600,
            "old_price": 1800,
            "rating": "4.8 (18 Reviews)",
            "description": "Elegant crochet bow handbag.",
            "material": "Cotton Yarn",
            "color": "Pink",
            "size": "Medium",
        },

        9: {
            "name": "Lilly Flower",
            "image": "app1/images/lilly.png",
            "price": 300,
            "old_price": 400,
            "rating": "4 (12 Reviews)",
            "description": "Handmade crochet lily flower.",
            "material": "Cotton Yarn",
            "color": "White",
            "size": "12 Inches",
        },

        10: {
            "name": "Cottagecore Top",
            "image": "app1/images/cottagecore.png",
            "price": 1700,
            "old_price": 1800,
            "rating": "4.5 (16 Reviews)",
            "description": "Stylish crochet cottagecore top.",
            "material": "Cotton Yarn",
            "color": "Cream",
            "size": "XS / S / M",
        },

        11: {
            "name": "Romper Set",
            "image": "app1/images/romper.png",
            "price": 2500,
            "old_price": 3000,
            "rating": "4.8 (15 Reviews)",
            "description": "Handmade crochet baby romper set.",
            "material": "Cotton Yarn",
            "color": "Blue",
            "size": "0-6 Months",
        },

        12: {
            "name": "Panda Keychain",
            "image": "app1/images/panda.png",
            "price": 399,
            "old_price": 499,
            "rating": "4.8 (18 Reviews)",
            "description": "Cute panda crochet keychain.",
            "material": "Cotton Yarn",
            "color": "Black & White",
            "size": "4 Inches",
        },

        13: {
            "name": "Scrunchies",
            "image": "app1/images/scrunchies.png",
            "price": 150,
            "old_price": 200,
            "rating": "4.8 (10 Reviews)",
            "description": "Handmade crochet scrunchies.",
            "material": "Cotton Yarn",
            "color": "Mixed",
            "size": "Free Size",
        },

        14: {
            "name": "Wine Rose",
            "image": "app1/images/winerose.png",
            "price": 650,
            "old_price": 700,
            "rating": "4.5 (12 Reviews)",
            "description": "Elegant crochet wine rose.",
            "material": "Cotton Yarn",
            "color": "Wine Red",
            "size": "12 Inches",
        },

        15: {
            "name": "Peplum Top",
            "image": "app1/images/peplumtop.png",
            "price": 2000,
            "old_price": 2500,
            "rating": "5 (20 Reviews)",
            "description": "Beautiful handmade crochet peplum top.",
            "material": "Cotton Yarn",
            "color": "Cream White",
            "size": "XS / S / M",
        },

        16: {
            "name": "Strawberry Keychain",
            "image": "app1/images/strawberry.png",
            "price": 299,
            "old_price": 399,
            "rating": "4.7 (14 Reviews)",
            "description": "Cute strawberry crochet keychain.",
            "material": "Cotton Yarn",
            "color": "Red",
            "size": "4 Inches",
        },

        17: {
            "name": "Tulip Headband",
            "image": "app1/images/tulipband.png",
            "price": 399,
            "old_price": 450,
            "rating": "5 (18 Reviews)",
            "description": "Stylish crochet tulip headband.",
            "material": "Cotton Yarn",
            "color": "Pink",
            "size": "Free Size",
        },

        18: {
            "name": "Tote Bag",
            "image": "app1/images/totebag.jpeg",
            "price": 1200,
            "old_price": 1300,
            "rating": "4.8 (18 Reviews)",
            "description": "Handmade crochet tote bag.",
            "material": "Cotton Yarn",
            "color": "Beige",
            "size": "Medium",
        },

                19: {
            "name": "Bandana",
            "image": "app1/images/bandana.png",
            "price": 399,
            "old_price": 499,
            "rating": "4.5 (20 Reviews)",
            "description": "Stylish handmade crochet bandana.",
            "material": "Cotton Yarn",
            "color": "Mixed",
            "size": "Free Size",
        },

        20: {
            "name": "Granny Square Bag",
            "image": "app1/images/bluebag.png",
            "price": 1899,
            "old_price": 1999,
            "rating": "5.0 (20 Reviews)",
            "description": "Beautiful handmade crochet granny square bag.",
            "material": "Cotton Yarn",
            "color": "Blue",
            "size": "Medium",
        },

        21: {
            "name": "Teddy Beanie",
            "image": "app1/images/cap.jpeg",
            "price": 299,
            "old_price": 399,
            "rating": "4.5 (20 Reviews)",
            "description": "Cute and cozy handmade crochet teddy beanie.",
            "material": "Cotton Yarn",
            "color": "Brown",
            "size": "Free Size",
        },

        22: {
            "name": "Cherry Bloosom",
            "image": "app1/images/cherrybloosam.png",
            "price": 399,
            "old_price": 499,
            "rating": "4.5 (20 Reviews)",
            "description": "Beautiful handmade crochet cherry blossom.",
            "material": "Cotton Yarn",
            "color": "Pink",
            "size": "12 Inches",
        },

        23: {
            "name": "Paw Keychain",
            "image": "app1/images/dog.jpeg",
            "price": 399,
            "old_price": 499,
            "rating": "4.5 (20 Reviews)",
            "description": "Cute handmade crochet paw keychain.",
            "material": "Cotton Yarn",
            "color": "Brown",
            "size": "4 Inches",
        },

        24: {
            "name": "Bunny Bloom Mobile",
            "image": "app1/images/hang.jpeg",
            "price": 799,
            "old_price": 899,
            "rating": "4.5 (20 Reviews)",
            "description": "Cute handmade crochet bunny bloom mobile.",
            "material": "Cotton Yarn",
            "color": "Mixed",
            "size": "Medium",
        },

        25: {
            "name": "Blossom Clip",
            "image": "app1/images/hairclip.png",
            "price": 199,
            "old_price": 299,
            "rating": "4.5 (20 Reviews)",
            "description": "Beautiful handmade crochet blossom hair clip.",
            "material": "Cotton Yarn",
            "color": "Pink",
            "size": "Free Size",
        },

        26: {
            "name": "Mocha Strip Shirt",
            "image": "app1/images/shirt.jpeg",
            "price": 1599,
            "old_price": 1699,
            "rating": "4.8 (20 Reviews)",
            "description": "Stylish handmade crochet mocha stripe shirt.",
            "material": "Cotton Yarn",
            "color": "Brown",
            "size": "S / M / L",
        },

        27: {
            "name": "Butterfly Bag",
            "image": "app1/images/butterflybag.png",
            "price": 1499,
            "old_price": 1599,
            "rating": "4.8 (20 Reviews)",
            "description": "Beautiful handmade crochet butterfly bag.",
            "material": "Cotton Yarn",
            "color": "Mixed",
            "size": "Medium",
        },

        28: {
            "name": "Rose",
            "image": "app1/images/rose.png",
            "price": 199,
            "old_price": 299,
            "rating": "4.8 (20 Reviews)",
            "description": "Beautiful handmade crochet rose.",
            "material": "Cotton Yarn",
            "color": "Red",
            "size": "12 Inches",
        },

        29: {
            "name": "Flower Clip",
            "image": "app1/images/clip.png",
            "price": 99,
            "old_price": 159,
            "rating": "4.8 (20 Reviews)",
            "description": "Cute handmade crochet flower clip.",
            "material": "Cotton Yarn",
            "color": "Mixed",
            "size": "Free Size",
        },

                30: {
            "name": "Hibiscus",
            "image": "app1/images/hibuscus.png",
            "price": 399,
            "old_price": 499,
            "rating": "4.8 (20 Reviews)",
            "description": "Beautiful handmade crochet hibiscus flower.",
            "material": "Cotton Yarn",
            "color": "Red",
            "size": "12 Inches",
        },

        31: {
            "name": "Ice Cream",
            "image": "app1/images/icecream.png",
            "price": 199,
            "old_price": 249,
            "rating": "4.8 (15 Reviews)",
            "description": "Cute handmade crochet ice cream.",
            "material": "Cotton Yarn",
            "color": "Mixed",
            "size": "4 Inches",
        },

        32: {
            "name": "Lavender",
            "image": "app1/images/lavender.png",
            "price": 299,
            "old_price": 399,
            "rating": "4.8 (18 Reviews)",
            "description": "Elegant handmade crochet lavender flower.",
            "material": "Cotton Yarn",
            "color": "Purple",
            "size": "12 Inches",
        },

        33: {
            "name": "Mushroom",
            "image": "app1/images/mushroom.png",
            "price": 169,
            "old_price": 219,
            "rating": "4.8 (14 Reviews)",
            "description": "Cute handmade crochet mushroom.",
            "material": "Cotton Yarn",
            "color": "Red & White",
            "size": "4 Inches",
        },

        34: {
            "name": "Sunflower",
            "image": "app1/images/sunflower.png",
            "price": 550,
            "old_price": 650,
            "rating": "4.8 (20 Reviews)",
            "description": "Beautiful handmade crochet sunflower.",
            "material": "Cotton Yarn",
            "color": "Yellow",
            "size": "12 Inches",
        },

        35: {
            "name": "Sweater",
            "image": "app1/images/sweater.png",
            "price": 750,
            "old_price": 899,
            "rating": "4.8 (16 Reviews)",
            "description": "Warm and stylish handmade crochet sweater.",
            "material": "Cotton Yarn",
            "color": "Cream",
            "size": "S / M / L",
        },

        36: {
            "name": "Teddy Romper",
            "image": "app1/images/teddyromper.jpeg",
            "price": 999,
            "old_price": 1199,
            "rating": "4.8 (18 Reviews)",
            "description": "Cute and soft handmade crochet teddy romper.",
            "material": "Cotton Yarn",
            "color": "Brown",
            "size": "0-6 Months",
        },
    }

    product = products.get(id)

    if not product:
        return redirect("shop")

    return render(request, "product_detail.html", {
        "product": product
    })


# =========================
# CUSTOM ORDER
# =========================@login_required(login_url="login")
def custom_order(request):

    if request.method == "POST":
        name = request.POST.get("full_name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        item = request.POST.get("product_type", "").strip()
        color = request.POST.get("color", "").strip()
        size = request.POST.get("size", "").strip()
        quantity = request.POST.get("quantity", 1)

        CustomOrder.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            email=email,
            item=item,
            color=color,
            size=size,
            quantity=quantity
        )

        messages.success(
            request,
            "Your custom order has been placed successfully! 🎉"
        )

        return redirect("account")

    return render(request, "custom_order.html")


# =========================
# ACCOUNT
# =========================
@login_required(login_url="login")
def account(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "login.html", {
        "cart_items": cart_items,
        "orders": orders
    })
# =========================
# LOGIN / SIGNUP
# =========================
def user_login(request):

    # If already logged in
    if request.user.is_authenticated:
        return redirect("account")

    # Remember the page user originally wanted
    next_url = request.GET.get("next") or request.POST.get("next")

    if request.method == "POST":

        action = request.POST.get("action")

        # =========================
        # SIGNUP
        # =========================
        if action == "signup":

            username = request.POST.get(
                "username", ""
            ).strip()

            email = request.POST.get(
                "email", ""
            ).strip()

            password = request.POST.get(
                "password", ""
            )

            if not username:

                return render(request, "login.html", {
                    "error": "Please enter your username.",
                    "next": next_url
                })

            if not password:

                return render(request, "login.html", {
                    "error": "Please enter your password.",
                    "next": next_url
                })

            if User.objects.filter(
                username=username
            ).exists():

                return render(request, "login.html", {
                    "error": "Username already exists.",
                    "next": next_url
                })

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            login(request, user)

            # Return to requested page
            if next_url:
                return redirect(next_url)

            return redirect("account")

        # =========================
        # LOGIN
        # =========================
        elif action == "login":

            username = request.POST.get(
                "username", ""
            ).strip()

            password = request.POST.get(
                "password", ""
            )

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                # Return to requested page
                if next_url:
                    return redirect(next_url)

                return redirect("account")

            return render(request, "login.html", {
                "error": "Invalid username or password.",
                "next": next_url
            })

    return render(request, "login.html", {
        "next": next_url
    })


# =========================
# LOGOUT
# =========================
def user_logout(request):

    logout(request)

    return redirect("login")


# =========================
# PLACE ORDER
# =========================
@login_required(login_url="login")
def place_order(request):

    if request.method != "POST":

        return JsonResponse({
            "success": False,
            "message": "Invalid request method."
        }, status=405)

    try:

        data = json.loads(request.body)

    except (json.JSONDecodeError, TypeError):

        return JsonResponse({
            "success": False,
            "message": "Invalid order data."
        }, status=400)

    first_name = str(
        data.get("first_name", "")
    ).strip()

    last_name = str(
        data.get("last_name", "")
    ).strip()

    phone = str(
        data.get("phone", "")
    ).strip()

    address = str(
        data.get("address", "")
    ).strip()

    notes = str(
        data.get("notes", "")
    ).strip()

    cart_items = data.get("cart", [])

    if not first_name:

        return JsonResponse({
            "success": False,
            "message": "Please enter your first name."
        }, status=400)

    if not phone:

        return JsonResponse({
            "success": False,
            "message": "Please enter your phone number."
        }, status=400)

    if not address:

        return JsonResponse({
            "success": False,
            "message": "Please enter your delivery address."
        }, status=400)

    if not isinstance(cart_items, list) or len(cart_items) == 0:

        return JsonResponse({
            "success": False,
            "message": "Your cart is empty."
        }, status=400)

    created_orders = []

    grand_total = Decimal("0.00")

    try:

        for item in cart_items:

            product_name = str(
                item.get("name", "")
            ).strip()

            image = str(
                item.get("image", "")
            ).strip()

            if not product_name:
                continue

            try:

                price = Decimal(
                    str(item.get("price", "0"))
                )

            except (
                InvalidOperation,
                TypeError,
                ValueError
            ):

                price = Decimal("0.00")

            try:

                quantity = int(
                    item.get("quantity", 1)
                )

            except (
                TypeError,
                ValueError
            ):

                quantity = 1

            if quantity < 1:
                quantity = 1

            if price < 0:
                price = Decimal("0.00")

            item_total = price * quantity

            order = Order.objects.create(

                user=request.user,

                first_name=first_name,

                last_name=last_name,

                phone=phone,

                address=address,

                notes=notes,

                product=product_name,

                price=price,

                quantity=quantity,

                total_amount=item_total,

                image=image
            )

            created_orders.append(order.id)

            grand_total += item_total

    except Exception:

        return JsonResponse({
            "success": False,
            "message": "Unable to place the order. Please try again."
        }, status=500)

    if not created_orders:

        return JsonResponse({
            "success": False,
            "message": "No valid products found in your cart."
        }, status=400)

    Cart.objects.filter(
        user=request.user
    ).delete()

    return JsonResponse({
        "success": True,
        "message": "Order placed successfully!",
        "order_ids": created_orders,
        "total": str(grand_total)
    })


# =========================
# MY ORDERS
# =========================
@login_required(login_url="login")
def orders(request):

    user_orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "orders.html", {
        "orders": user_orders
    })


# =========================
# ADD TO CART
# =========================
@login_required(login_url="login")
def add_to_cart(request):

    if request.method == "POST":

        product = request.POST.get("product")

        price = request.POST.get("price")

        quantity = request.POST.get(
            "quantity", 1
        )

        image = request.POST.get("image")

        existing_item = Cart.objects.filter(
            user=request.user,
            product=product
        ).first()

        if existing_item:

            existing_item.quantity += int(quantity)

            existing_item.save()

        else:

            Cart.objects.create(
                user=request.user,
                product=product,
                price=price,
                quantity=quantity,
                image=image
            )

    return redirect("cart")


# =========================
# CART PAGE
# =========================
@login_required(login_url="login")
def cart(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    return render(request, "cart.html", {
        "cart_items": cart_items
    })


# =========================
# CHECKOUT
# =========================
@login_required(login_url="login")
def checkout(request):

    return render(request, "checkout.html")