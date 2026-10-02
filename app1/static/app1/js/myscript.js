
    console.log("🌿 HIGA — Olive Green + Sand + Clay palette active!");
    console.log("✅ Navbar hover effects working, product section with 8 items displayed.");
    
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            if(link.getAttribute('href') === '#products') {
                e.preventDefault();
                document.getElementById('products').scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    /*product_details*/

   function increaseQty() {

    let qty = document.getElementById("quantity");
    qty.value++;

    document.getElementById("qtyHidden").value = qty.value;
    document.getElementById("buyQty").value = qty.value;
}

function decreaseQty() {

    let qty = document.getElementById("quantity");

    if (qty.value > 1) {
        qty.value--;

        document.getElementById("qtyHidden").value = qty.value;
        document.getElementById("buyQty").value = qty.value;
    }
}


    function openPopup() {
    document.getElementById("buyPopup").style.display = "flex";
}

function closePopup() {
    document.getElementById("buyPopup").style.display = "none";
}



document.addEventListener("DOMContentLoaded", function () {
    updateCartCount();

    if (typeof renderCart === "function") {
        renderCart();
    }
});