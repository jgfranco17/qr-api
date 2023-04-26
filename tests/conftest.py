import pytest
from api import create_server


@pytest.fixture(scope="module")
def client():
    """
    Create a test client for the FastAPI app
    """
    app = create_server()
    with app.test_client() as test_client:
        yield test_client
