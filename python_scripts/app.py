from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure database connection from environment variables
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.environ.get('POSTGRES_USER')}:"
    f"{os.environ.get('POSTGRES_PASSWORD')}@"
    f"{os.environ.get('POSTGRES_HOST')}:"
    f"{os.environ.get('POSTGRES_PORT')}/"
    f"{os.environ.get('POSTGRES_DB')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Example API routes
@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "message": "StealHouse API is running"})


@app.route("/api/properties", methods=["GET"])
def get_properties():
    # This is a placeholder - you'll need to implement your actual data retrieval
    # from your database models
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
