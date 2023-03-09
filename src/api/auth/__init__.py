"""Module contains Auth implementations for the API."""
import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


class AuthConfig:
    """Contains Auth Configurations"""

    basic: HTTPBasic = HTTPBasic(
        scheme_name="basic",
        description="Basic Auth",
        realm=None,
        auto_error=True,
    )


class Auth:
    """Container holding all Auth implementations."""

    @staticmethod
    def basic(credentials: HTTPBasicCredentials = Depends(AuthConfig.basic)):
        """Basic Auth Implementation"""
        valid_credentials = all(
            [
                secrets.compare_digest(credentials.username.encode("utf8"), b"admin"),
                secrets.compare_digest(credentials.password.encode("utf8"), b"admin"),
            ]
        )
        if not valid_credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )

        return credentials.username
