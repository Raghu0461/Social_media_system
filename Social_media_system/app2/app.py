from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# The User Profile Service URL (you'll need to replace this with the correct IP or DNS if deploying in separate clusters)
USER_PROFILE_SERVICE_URL = "http://app1:8000/users"  # Use app1 as the hostname when using Docker Compose

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_details(user_id):
    user_response = requests.get(f"{USER_PROFILE_SERVICE_URL}/{user_id}")
    if user_response.status_code == 200:
        return jsonify(user_response.json())
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
