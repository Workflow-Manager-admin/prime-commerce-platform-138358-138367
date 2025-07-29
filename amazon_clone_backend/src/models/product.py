from pydantic import BaseModel, Field
from typing import Optional

# PUBLIC_INTERFACE
class ProductBase(BaseModel):
    """Base schema for product information."""
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Product price")
    image_url: Optional[str] = Field(None, description="URL of the product image")
    in_stock: bool = Field(..., description="Availability status")

# PUBLIC_INTERFACE
class ProductCreate(ProductBase):
    """Schema for product creation."""
    pass

# PUBLIC_INTERFACE
class ProductUpdate(ProductBase):
    """Schema for updating products."""
    name: Optional[str]
    price: Optional[float]
    in_stock: Optional[bool]

# PUBLIC_INTERFACE
class Product(ProductBase):
    """Schema for product output with ID."""
    id: int
