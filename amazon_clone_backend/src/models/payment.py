from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class PaymentRequest(BaseModel):
    """Schema for initiating a payment request."""
    order_id: int
    amount: float
    method: str = Field(..., description="Payment method, e.g. 'credit_card', 'paypal'.")

# PUBLIC_INTERFACE
class PaymentResponse(BaseModel):
    """Schema for payment status response."""
    payment_id: int
    status: str
    detail: str = ""
