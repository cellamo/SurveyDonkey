# Survey Donkey Project Setup

This document outlines the setup process for both the backend (Django) and frontend (React) development environments for the Survey Donkey project.

## Prerequisites

Before you begin, ensure you have the following installed on your local development machine:
- Python 3
- pip (Python package installer)
- Node.js and npm (Node package manager)
- git 

## Backend Setup (Django)

1. **Clone the Repository**:
   Begin by cloning the project repository to your local machine using git.
   ```
   git clone git@github.com:your-username/SurveyDonkey.git
   cd SurveyDonkey
   ```

2. **Install Dependencies**:
   Install the required Python packages using `pip`:
   ```
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Set the `DATABASE_URL` environment variable to connect to the Heroku PostgreSQL database.
   
   - On macOS/Linux:
     ```
     export DATABASE_URL='your_heroku_postgres_url'
     ```
   - On Windows CMD:
     ```
     set DATABASE_URL=your_heroku_postgres_url
     ```
   - On Windows PowerShell:
     ```
     $env:DATABASE_URL="your_heroku_postgres_url"
     ```

   **Note:** Replace `your_heroku_postgres_url` with the actual database URL.

4. **Database Migration**:
   Apply the database migrations to create the necessary database tables:
   ```
   python manage.py migrate
   ```

5. **Running the Development Server**:
   Start the Django development server using the following command:
   ```
   python manage.py runserver
   ```

   The server will start on `http://127.0.0.1:8000/` by default.

## Frontend Setup (React)

1. **Navigate to the Client Directory**:
   ```
   cd client
   ```

2. **Install Node Modules**:
   Use `npm` to install the necessary node modules:
   ```
   npm install
   ```

3. **Start the React Development Server**:
   Once the node modules are installed, start the development server:
   ```
   npm start
   ```

   The React application will start on `http://localhost:3000/` by default.

## Important Notes

- Do **not** commit any secret keys, the `DATABASE_URL`, or `node_modules` to the git repository.
- Ensure you are using a virtual environment for Python and the correct node version for JavaScript dependencies to avoid conflicts with other projects or system packages.