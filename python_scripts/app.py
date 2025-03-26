from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Keep for local development
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure database connection from environment variables
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.environ.get('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "message": "StealHouse API is running"})


@app.route("/api/properties", methods=["GET"])
def get_properties():
    return jsonify(
        {
            "properties": [
                {
                    "id": 1,
                    "title": "Modern Apartment in City Center",
                    "address": "123 Main Street",
                    "price": 1200,
                    "size": 75,
                    "bedrooms": 2,
                    "bathrooms": 1,
                },
                {
                    "id": 2,
                    "title": "Spacious Family Home",
                    "address": "456 Park Avenue",
                    "price": 1800,
                    "size": 120,
                    "bedrooms": 3,
                    "bathrooms": 2,
                },
            ]
        }
    )


# Add more API routes as needed for your application

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
