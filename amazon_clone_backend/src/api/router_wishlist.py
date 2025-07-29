from fastapi import APIRouter, Depends
from src.models.wishlist import WishlistItem, WishlistOut
from src.api.deps import get_current_user

router = APIRouter(prefix="/wishlist", tags=["wishlist"])

# PUBLIC_INTERFACE
@router.get("/", response_model=WishlistOut, summary="Get user's wishlist")
def get_wishlist(current_user=Depends(get_current_user)):
    """Get the user's wishlist."""
    # Placeholder: Replace with DB logic
    return WishlistOut(user_id=current_user["id"], items=[])

# PUBLIC_INTERFACE
@router.post("/add", response_model=WishlistOut, summary="Add product to wishlist")
def add_to_wishlist(item: WishlistItem, current_user=Depends(get_current_user)):
    """Add product to user's wishlist."""
    # Placeholder: DB logic to add to wishlist
    return WishlistOut(user_id=current_user["id"], items=[item])

# PUBLIC_INTERFACE
@router.post("/remove", response_model=WishlistOut, summary="Remove product from wishlist")
def remove_from_wishlist(item: WishlistItem, current_user=Depends(get_current_user)):
    """Remove product from user's wishlist."""
    # Placeholder: DB logic to remove from wishlist
    return WishlistOut(user_id=current_user["id"], items=[])
