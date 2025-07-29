from fastapi import APIRouter, Depends
from src.models.payment import PaymentRequest, PaymentResponse
from src.api.deps import get_current_user

router = APIRouter(prefix="/payments", tags=["payments"])

# PUBLIC_INTERFACE
@router.post("/", response_model=PaymentResponse, summary="Create payment intent")
def create_payment(payment: PaymentRequest, current_user=Depends(get_current_user)):
    """
    Create payment intent for an order.
    Integrate here with Stripe/PayPal/etc.
    """
    # Placeholder: Implement payment gateway here
    return PaymentResponse(payment_id=1, status="succeeded", detail="Paid successfully")
