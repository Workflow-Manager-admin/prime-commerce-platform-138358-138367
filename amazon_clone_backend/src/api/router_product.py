from fastapi import APIRouter, HTTPException, Query
from src.models.product import Product, ProductCreate
from typing import List, Optional

router = APIRouter(prefix="/products", tags=["products"])

# PUBLIC_INTERFACE
@router.get("/", response_model=List[Product], summary="List/search products", description="List all products or search by keyword.")
def list_products(q: Optional[str] = Query(None, description="Search keyword")):
    """List all products or search by keyword."""
    # Placeholder: Add search logic
    return []

# PUBLIC_INTERFACE
@router.post("/", response_model=Product, summary="Create product", description="Add a new product to the catalog.")
def create_product(product: ProductCreate):
    """Create a new product."""
    # Placeholder: Add insert-to-db logic
    return Product(id=1, **product.dict())

# PUBLIC_INTERFACE
@router.get("/{product_id}", response_model=Product, summary="Get product by ID", description="Retrieve a product by its ID.")
def get_product(product_id: int):
    """Get product by ID."""
    # Placeholder: Add get-from-db logic
    if product_id == 1:
        return Product(id=1, name="Sample Product", description="Test desc", price=99.99, image_url=None, in_stock=True)
    raise HTTPException(status_code=404, detail="Product not found")
