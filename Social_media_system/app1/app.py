from flask import Flask, jsonify

app = Flask(__name__)

# Sample user profiles
user_profiles = {
    1: {"name": "Alice", "email": "alice@example.com", "profile_picture": "alice.png", "interests": ["Music", "Photography"]},
    2: {"name": "Bob", "email": "bob@example.com", "profile_picture": "bob.png", "interests": ["Gaming", "Technology"]},
    3: {"name": "Charlie", "email": "charlie@example.com", "profile_picture": "charlie.png", "interests": ["Travel", "Sports"]},
}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = user_profiles.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
