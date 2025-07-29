from fastapi import APIRouter, Depends
from src.models.user import UserCreate, UserLogin, UserOut
from src.api.deps import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

# PUBLIC_INTERFACE
@router.post("/register", response_model=UserOut, summary="Register a new user", description="Register a new user account.")
def register(user: UserCreate):
    """Register a new user."""
    # Placeholder: Add insert-to-db logic
    return UserOut(id=1, email=user.email, full_name=user.full_name, is_active=True)

# PUBLIC_INTERFACE
@router.post("/login", summary="Login user and return JWT", description="Authenticate user and return auth token.")
def login(user: UserLogin):
    """Authenticate user and return token."""
    # Placeholder: Add auth logic and JWT generation
    return {"access_token": "sample.jwt.token", "token_type": "bearer"}

# PUBLIC_INTERFACE
@router.get("/me", response_model=UserOut, summary="Get current user details")
def get_me(current_user=Depends(get_current_user)):
    """Get current logged in user."""
    return current_user
