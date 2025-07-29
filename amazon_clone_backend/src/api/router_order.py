from fastapi import APIRouter, Depends
from typing import List
from src.models.order import OrderCreate, OrderOut
from src.api.deps import get_current_user
from datetime import datetime

router = APIRouter(prefix="/orders", tags=["orders"])

# PUBLIC_INTERFACE
@router.post("/checkout", response_model=OrderOut, summary="Checkout and create order")
def checkout(order: OrderCreate, current_user=Depends(get_current_user)):
    """Create an order from the current cart."""
    # Placeholder: Real DB/payment logic goes here
    return OrderOut(
        id=1,
        user_id=current_user["id"],
        items=order.items,
        status="pending",
        created_at=datetime.utcnow(),
        total_price=100.0
    )

# PUBLIC_INTERFACE
@router.get("/history", response_model=List[OrderOut], summary="Get order history")
def order_history(current_user=Depends(get_current_user)):
    """Get order history for the current user."""
    # Placeholder: replace with DB logic
    return []

# PUBLIC_INTERFACE
@router.get("/{order_id}/track", response_model=str, summary="Track order status")
def track_order(order_id: int, current_user=Depends(get_current_user)):
    """Track order status."""
    # Placeholder: replace with DB logic
    return "Shipped"
