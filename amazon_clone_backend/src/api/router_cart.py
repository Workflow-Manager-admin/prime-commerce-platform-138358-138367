from fastapi import APIRouter, Depends
from src.models.cart import CartCreate, CartOut, CartProduct
from src.api.deps import get_current_user

router = APIRouter(prefix="/cart", tags=["cart"])

# PUBLIC_INTERFACE
@router.get("/", response_model=CartOut, summary="Get shopping cart", description="Get the current user's shopping cart.")
def get_cart(current_user=Depends(get_current_user)):
    """Retrieve the user's current shopping cart."""
    # Placeholder: Replace with DB logic
    return CartOut(user_id=current_user["id"], items=[])

# PUBLIC_INTERFACE
@router.post("/add", response_model=CartOut, summary="Add item to cart", description="Add a product to the cart.")
def add_to_cart(item: CartCreate, current_user=Depends(get_current_user)):
    """Add a product to the user's cart."""
    # Placeholder: DB logic to add to cart
    return CartOut(user_id=current_user["id"], items=[
        CartProduct(product_id=item.product_id, quantity=item.quantity)
    ])

# PUBLIC_INTERFACE
@router.post("/remove", response_model=CartOut, summary="Remove item from cart", description="Remove a product from the cart.")
def remove_from_cart(item: CartCreate, current_user=Depends(get_current_user)):
    """Remove a product from the user's cart."""
    # Placeholder: DB logic to remove from cart
    return CartOut(user_id=current_user["id"], items=[])
