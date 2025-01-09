# project-pzaw

A school project using Django framework and Svelte for frontend.
Typeracer, where you can test your typing, calculating WPM and storing in user data.
Maybe some day I'll deploy this (i've tried).

## How to Run This App

### Backend (Django)

1. **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Collect static files**:
    ```bash
    python manage.py collectstatic --no-input
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

### Frontend (Svelte)

1. **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2. **Install the required packages**:
    ```bash
    npm install
    ```

3. **Run the development server**:
    ```bash
    npm run dev
    ```

### Access the App

- **Backend**: The Django backend will be running at `http://127.0.0.1:8000/`.
- **Frontend**: The Svelte frontend will be running at `http://localhost:5000/`.

Make sure both servers are running simultaneously to access the full functionality of the app.