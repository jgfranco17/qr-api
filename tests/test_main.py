import io
import requests
import pytest
import qrcode
from PIL import Image
from .conftest import client


def test_root_endpoint(client):
    """
    Test the root endpoint.
    """
    response = client.get("/")
    assert response.status_code == 200, "Client should be able to access the root endpoint."


def test_get_nonexistent_endpoint(client):
    """
    Test getting a nonexistent endpoint.
    """
    response = client.get("/non-existent")
    assert response.status_code == 404, "This endpoint does not exist in the architecture and should fail."
    
    
@pytest.mark.parametrize(
    "host",
    [   "www.google.com",
        "example.com",
        "example.org"
    ],
)
def test_network_connectivity(host):
    """
    Test internal and external network interactivity using multiple domains.
    """
    response = requests.get(f"http://{host}")
    assert response.status_code == 200, "Client should be able to reach this domain if connected to network."
    
    
def test_valid_qrcode(client):
    """
    Test that a valid QR code is returned.
    """
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data("https://example.com")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    expected_bytes = io.BytesIO()
    img.save(expected_bytes, format="PNG")
    expected_bytes.seek(0)

    response = client.get("/qrcode?url=https://example.com")
    assert response.status_code == 200, "Valid endpoint should generate image."


def test_empty_qrcode_data(client):
    """
    Test that an error is returned for empty QR code data.
    """
    response = client.get("/qrcode?url=")
    assert response.status_code == 400, "Empty parameter should fail as endpoint."