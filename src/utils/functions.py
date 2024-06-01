import os
import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

user_docs: str = os.environ.get("USER_DOCS")
password_docs: str = os.environ.get("PASSWORD_DOCS")


def get_current_username_docs(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Verify the current user's credentials using HTTP Basic Authentication.

    This function compares the provided username and password against predefined
    values (`user_docs` and `password_docs`). If the credentials are correct, it
    returns the username; otherwise, it raises an HTTP 401 Unauthorized exception.

    Parameters
    ----------
    credentials : HTTPBasicCredentials, optional
        An instance of HTTPBasicCredentials that holds the username and password
        provided by the user. This parameter is automatically injected by FastAPI
        using the Depends function and a security dependency.

    Returns
    -------
    str
        The username if the provided credentials are correct.

    Raises
    ------
    HTTPException
        If the provided username or password is incorrect, an HTTP 401 Unauthorized
        exception is raised with the appropriate status code, detail message, and
        headers indicating that Basic Authentication is required.
    """
    correct_username = secrets.compare_digest(credentials.username, user_docs)
    correct_password = secrets.compare_digest(credentials.password, password_docs)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect users or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
