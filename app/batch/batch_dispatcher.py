import requests

from app.call_generator.generate_calls import generate_device_interaction


def send_batch(batch_size, endpoint):
    batch = [generate_device_interaction() for _ in range(batch_size)]
    headers = {"Content-Type": "application/json"}

    try:
        requests.post(endpoint, json=batch, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"Failed to send batch: {e}")


# Configuration
API_ENDPOINT = "http://localhost:5000/api/phone_tracker"
BATCH_SIZE = 10  # Number of interactions in each batch