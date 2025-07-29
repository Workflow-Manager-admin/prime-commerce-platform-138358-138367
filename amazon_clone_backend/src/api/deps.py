from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os

SECRET_KEY = os.getenv("SECRET_KEY", "changeme") # Strong key in production
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Stub user loader for example
def fake_get_user(email: str):
    # Replace this with actual DB logic in production
    return {"email": email, "full_name": "Test User", "id": 1, "is_active": True}

# PUBLIC_INTERFACE
def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get currently authenticated user from JWT token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = fake_get_user(email)
    if user is None:
        raise credentials_exception
    return user
