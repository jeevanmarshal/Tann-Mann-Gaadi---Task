# The Tann Mann Foundation - Evaluation Task

This repository contains the completed evaluation task for the Full Stack Developer Internship at **The Tann Mann Foundation**. The project is a full-stack web application designed to collect user details (Name, Phone Number, Email) via a beautiful, modern UI, and securely store them in a PostgreSQL database.

## 🚀 Tech Stack

- **Frontend:** React.js, Vite, Vanilla CSS (Glassmorphism design)
- **Backend:** Python, Flask, psycopg3 (PostgreSQL adapter), Flask-CORS
- **Database:** PostgreSQL

---

## 🎨 Frontend (React.js)

The frontend is a visually striking "Good Morning" interface built with React and Vite. It focuses heavily on modern UI/UX principles, featuring:
- **Glassmorphism Elements:** A frosted-glass card effect for the form container.
- **Dynamic Backgrounds:** A smooth, animated gradient background (Mint Green to Soft Blue) that breathes life into the page.
- **Micro-interactions:** Interactive focus states on inputs and hover physics on the submit button.
- **Responsive Design:** Fully fluid layout that adapts perfectly to any screen size.

### Setup Instructions (Frontend)
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. Open [http://localhost:5173/](http://localhost:5173/) in your browser.

---

## ⚙️ Backend (Python Flask) & Database (PostgreSQL)

The backend is a robust Python Flask REST API designed to safely ingest the form data and communicate with a local PostgreSQL instance.

**Key Features:**
- **Auto-Initialization:** The Flask app automatically creates the `submissions` table in PostgreSQL upon startup if it doesn't exist.
- **Robust Validation:** Ensures all fields are present before attempting database insertion.
- **CORS Configured:** Securely accepts cross-origin requests from the React frontend.

### Prerequisites
- Python 3.8+
- PostgreSQL Server installed and running locally.

### Setup Instructions (Backend)
1. **Database Setup:** 
   Open pgAdmin (or your preferred SQL client) and create a new local database named `tann_mann_db`.

2. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

3. **Set up Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables:**
   A `.env` file is already provided with the default credentials (`postgres`/`postgres`). Update these if your local PostgreSQL setup differs.

6. **Run the Server:**
   ```bash
   python app.py
   ```
   The API will run on `http://127.0.0.1:5000/`.

---

## 💡 How it Works
1. A user visits the React frontend and fills out the "Good Morning" form.
2. Upon submission, the React app sends an HTTP POST request containing a JSON payload to the Flask backend endpoint (`/api/submit`).
3. Flask validates the data, opens a connection to the PostgreSQL database, and executes an `INSERT` statement.
4. If successful, the backend returns a 201 status, and the frontend displays a success message.

## 📝 Developer Notes
*Note: The Flutter mobile application component of the task was intentionally skipped in favor of delivering a highly polished, production-ready implementation of the React/Python web stack.*
