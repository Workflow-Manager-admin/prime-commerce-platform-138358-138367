from pydantic import BaseModel
from typing import List

# PUBLIC_INTERFACE
class WishlistItem(BaseModel):
    """Schema for a product entry in the wishlist."""
    product_id: int

# PUBLIC_INTERFACE
class WishlistOut(BaseModel):
    """Schema for returning user's wishlist."""
    user_id: int
    items: List[WishlistItem]
