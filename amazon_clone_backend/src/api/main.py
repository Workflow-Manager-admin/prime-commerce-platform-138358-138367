from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.router_user import router as user_router
from src.api.router_product import router as product_router
from src.api.router_cart import router as cart_router
from src.api.router_wishlist import router as wishlist_router
from src.api.router_order import router as order_router
from src.api.router_payment import router as payment_router
from src.api.router_email import router as email_router

app = FastAPI(
    title="Amazon Clone E-commerce API",
    description="RESTful API for an Amazon-inspired e-commerce platform developed with FastAPI.",
    version="1.0.0",
    openapi_tags=[
        {"name": "users", "description": "User registration, authentication, and profile"},
        {"name": "products", "description": "Product catalog and search"},
        {"name": "cart", "description": "Shopping cart management"},
        {"name": "wishlist", "description": "Wishlist management"},
        {"name": "orders", "description": "Order history, checkout, and tracking"},
        {"name": "payments", "description": "Payment processing"},
        {"name": "email", "description": "Email notifications"}
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {"message": "Healthy"}

# Include routers for each domain
app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(wishlist_router)
app.include_router(order_router)
app.include_router(payment_router)
app.include_router(email_router)
