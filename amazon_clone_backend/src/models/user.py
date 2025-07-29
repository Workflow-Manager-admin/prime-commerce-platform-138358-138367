from pydantic import BaseModel, EmailStr, Field

# PUBLIC_INTERFACE
class UserBase(BaseModel):
    """Base schema for user information."""
    email: EmailStr = Field(..., description="User's email address")
    full_name: str = Field(..., description="User's full name")

# PUBLIC_INTERFACE
class UserCreate(UserBase):
    """Schema for user registration."""
    password: str = Field(..., description="User's password for registration")

# PUBLIC_INTERFACE
class UserLogin(BaseModel):
    """Schema for user login."""
    email: EmailStr
    password: str

# PUBLIC_INTERFACE
class UserOut(UserBase):
    """Schema for user response."""
    id: int
    is_active: bool

# PUBLIC_INTERFACE
class UserInDB(UserOut):
    """Database user schema (internal)."""
    hashed_password: str
