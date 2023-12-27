### SurveyDonkey API Documentation

#### Base URL
`http://localhost:8000/api/`

#### Authentication
Most endpoints require authentication. Users must be logged in to access these endpoints. Authentication is performed via token. Include the token in the header as `Authorization: Token <your-token>`.

#### API Endpoints

1. **List/Create Surveys**
   - **Endpoint**: `/api/surveys/`
   - **Method**: GET/POST
   - **Description**: Retrieve a list of all surveys or create a new survey.
   - **Permissions**: Authenticated Users
   - **POST Data**: `{ "title": "<title>", "description": "<description>", "end_time": "<YYYY-MM-DDTHH:MM:SS>" }`
   - **Response**: 
     - GET: `[{"id": 1, "title": "Survey Title", "description": "Description", ...}, ...]`
     - POST: `{"id": 1, "title": "Survey Title", "description": "Description", ...}`

2. **Retrieve/Update/Delete Survey**
   - **Endpoint**: `/api/surveys/<int:pk>/`
   - **Method**: GET/PUT/DELETE
   - **Description**: Retrieve, update, or delete a specific survey.
   - **Permissions**: Authenticated Users, Survey Creators
   - **Response**: 
     - GET/PUT: `{"id": 1, "title": "Survey Title", "description": "Description", ...}`
     - DELETE: `HTTP 204 No Content`

3. **Send Survey Invitations**
   - **Endpoint**: `/api/surveys/<int:pk>/send-invitations/`
   - **Method**: POST
   - **Description**: Send invitations to participate in a survey.
   - **POST Data**: `{ "emails": ["email1@example.com", "email2@example.com"] }`
   - **Permissions**: Authenticated Users, Survey Creators
   - **Response**: `{"message": "Invitations sent"}`

4. **List User's Surveys**
   - **Endpoint**: `/api/my-surveys/`
   - **Method**: GET
   - **Description**: Retrieve a list of surveys created by the authenticated user.
   - **Permissions**: Authenticated Users
   - **Response**: `[{"id": 1, "title": "Survey Title", "description": "Description", ...}, ...]`

5. **User Registration**
   - **Endpoint**: `/api/register/`
   - **Method**: POST
   - **Description**: Register a new user.
   - **POST Data**: `{ "email": "<email>" }`
   - **Response**: `{"message": "Registration email sent. Check your inbox."}`

6. **User Login**
   - **Endpoint**: `/api/login/`
   - **Method**: POST
   - **Description**: Login for existing users.
   - **POST Data**: `{ "email": "<email>" }`
   - **Response**: `{"message": "Login email sent. Check your inbox."}`

7. **Token Verification**
   - **Endpoint**: `/api/verify-token/<str:token>/`
   - **Method**: GET
   - **Description**: Verify user login token.
   - **Permissions**: Public Access
   - **Response**: `{"message": "Token verified successfully"}`

8. **Answer Survey**
   - **Endpoint**: `/api/answer-survey/<int:survey_id>/<str:token>/`
   - **Method**: GET
   - **Description**: Access a survey to provide answers.
   - **Permissions**: Users with a valid invitation token
   - **Response**: `{ "survey": { "id": 1, "title": "Survey Title", ... }, "questions": [{ "id": 1, "text": "Question?", ...}, ...]}`