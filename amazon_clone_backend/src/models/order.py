from pydantic import BaseModel
from typing import List
from datetime import datetime

# PUBLIC_INTERFACE
class OrderItem(BaseModel):
    """Schema for an item in an order."""
    product_id: int
    quantity: int

# PUBLIC_INTERFACE
class OrderCreate(BaseModel):
    """Schema for creating an order during checkout."""
    items: List[OrderItem]
    payment_method: str

# PUBLIC_INTERFACE
class OrderOut(BaseModel):
    """Schema for returning order information."""
    id: int
    user_id: int
    items: List[OrderItem]
    status: str
    created_at: datetime
    total_price: float
