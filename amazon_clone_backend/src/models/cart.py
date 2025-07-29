from pydantic import BaseModel, Field
from typing import List

# PUBLIC_INTERFACE
class CartProduct(BaseModel):
    """Schema for a product in the cart."""
    product_id: int
    quantity: int = Field(..., gt=0)

# PUBLIC_INTERFACE
class CartCreate(BaseModel):
    """Schema for adding products to cart."""
    product_id: int
    quantity: int = Field(..., gt=0)

# PUBLIC_INTERFACE
class CartOut(BaseModel):
    """Schema for returning cart info."""
    user_id: int
    items: List[CartProduct]
