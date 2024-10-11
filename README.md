# FastAPI Google OAuth2 Project

This is a FastAPI project that integrates Google OAuth2 for authentication.

## Features

- Google OAuth2 authentication
- Secure user login
- Simple API structure

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- HTTPX
- Google Auth(google-auth)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/denizparlak1/fastapi-google-auth.git
   cd fastapi-google-auth

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
    ```bash
    pip install -r requirements.txt

4. Set up your Google Cloud project:
   - Go to the Google Cloud Console.
   - Create a new project.
   - Navigate to "APIs & Services" > "Credentials".
   - Create an OAuth 2.0 Client ID and set the redirect URI (e.g., http://localhost:8000/api/authentication/callback).
   - Download the credentials JSON file and save it as credentials.json.


5. Set environment variables:
    ```bash
    export GOOGLE_CLIENT_ID='your-client-id'
    export GOOGLE_CLIENT_SECRET='your-client-secret'
    export SECRET_KEY='your_secret_key'
   
## Running the Application
To start the FastAPI application, run:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000
