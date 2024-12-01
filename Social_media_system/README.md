# Social Media System

This project consists of two Flask-based applications:

- **App1 (User Profile Service)**: Provides user profiles at the `/users/<user_id>` endpoint.
- **App2 (Fetching User Details)**: Fetches user details from App1 by calling its `/users/<user_id>` endpoint.

## Running the Applications

### With Docker Compose

1. Build and start the services:

   ```bash
   docker-compose up --build
