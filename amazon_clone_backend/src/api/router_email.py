from fastapi import APIRouter

router = APIRouter(prefix="/email", tags=["email"])

# PUBLIC_INTERFACE
@router.post("/send", summary="Send email", description="Send a notification or order confirmation email.")
def send_email(to: str, subject: str, body: str):
    """
    Stub endpoint: Email notifications.
    Real implementation should use a provider like SendGrid.
    """
    # Placeholder: Implement actual email sending logic
    return {"status": "sent", "to": to, "subject": subject}
