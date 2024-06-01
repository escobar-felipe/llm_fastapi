import logging

from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def handle_error(error: Exception):
    """
    Handle and log an unexpected error, returning a JSON response.

    This function logs the provided error message and returns a JSON response
    with a status code of 500, indicating an internal server error. The response
    includes a generic error message.

    Parameters
    ----------
    error : Exception
        The exception that occurred.

    Returns
    -------
    JSONResponse
        A JSON response with a status code of 500 and a message indicating that
        an unexpected error occurred.
    """
    # Log the error
    logger.error(f"Error occurred: {error}")
    # Customize the response if needed
    return JSONResponse(
        status_code=500, content={"detail": "An unexpected error occurred."}
    )
