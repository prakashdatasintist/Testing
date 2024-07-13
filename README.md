# ZentraTech Developer Test 2024

## Setup Instructions

### Backend

1. Clone the repository
2. Navigate to the `zentratech` directory
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the server: `python manage.py runserver`

### Frontend

1. Navigate to the `zentratech-frontend` directory
2. Install dependencies: `npm install`
3. Run the app: `npm start`

## Design Choices

- Used Django for the backend to leverage its built-in authentication and admin interface.
- Chose React for the frontend for its component-based architecture and ease of state management.
- Used Axios for making HTTP requests to the Django REST API.
- Implemented user authentication, interest messaging, and real-time chat as core features.
- Emphasized simplicity and clarity in the code to ensure maintainability.

## Next Steps

- Enhance the chat system with WebSocket for real-time communication.
- Improve the UI/UX with better styling and user feedback.
- Add pagination and filtering to user and message lists.
- Write more comprehensive tests to cover edge cases and improve code coverage.
