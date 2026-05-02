import os
import psycopg
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Allow CORS for the frontend to communicate with the backend
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Database connection details
DB_NAME = os.getenv("DB_NAME", "tann_mann_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_db_connection():
    """Establish and return a connection to the PostgreSQL database."""
    conn = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def init_db():
    """Initialize the database by creating the required table if it doesn't exist."""
    conn = get_db_connection()
    cur = conn.cursor()
    # Create the submissions table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(50) NOT NULL,
            email VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

# Try to initialize the database table when the app starts
try:
    init_db()
    print("Database connected and table initialized successfully!")
except Exception as e:
    print(f"Warning: Database initialization error (make sure PostgreSQL is running): {e}")

@app.route('/api/submit', methods=['POST'])
def submit_form():
    """Endpoint to handle form submissions and save to PostgreSQL."""
    try:
        data = request.json
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        # Basic validation
        if not all([name, phone, email]):
            return jsonify({'error': 'All fields are required!'}), 400

        # Save to database
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(
            'INSERT INTO submissions (name, phone, email) VALUES (%s, %s, %s) RETURNING id',
            (name, phone, email)
        )
        new_id = cur.fetchone()[0]
        
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({
            'message': 'Details submitted successfully!', 
            'id': new_id
        }), 201
    
    except psycopg.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    return jsonify({'status': 'Flask backend is running!'})

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True, port=5000)
