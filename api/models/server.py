import io
import qrcode
from flask import Flask, request, make_response, jsonify


def create_server() -> Flask:
    """
    Creates an instance of the API app.

    Returns:
        Flask: API app unit
    """
    app = Flask(__name__)

    def validate_url(url: str) -> tuple:
        """
        Validates the given endpoint.

        Args:
            url (str): _description_

        Returns:
            tuple: returns validity, as well as message and error code if needed
        """
        if url is None or url.strip() == "":
            return (False, jsonify({'message': 'Invalid data for QR code'}), 400)
        return (True, None, None)

    @app.route("/", methods=['GET'])
    def root():
        return "<h1>Welcome to the URL QR converter!</h1>"

    @app.route("/qrcode", methods=['GET'])
    def generate_qr():
        response = (jsonify({'message': 'Invalid data for QR code'}), 400)
        try:
            url = request.args.get("url")
            valid, error_response, error_code = validate_url(url)
            if not valid:
                return error_response, error_code

            qr = qrcode.make(url)
            buffer = io.BytesIO()
            qr.save(buffer, format="PNG")
            buffer.seek(0)
            response = make_response(buffer.getvalue())
            response.mimetype = "image/png"

        except Exception as e:
            print(f'Failed to provide a QR code: {e}')

        return response, 200

    return app
