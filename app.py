from flask import Flask
import sqlite3
import os

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'data','database.db');

def init_db():
    db_path = app.config['DATABASE']
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    db = sqlite3.connect(db_path)
    schema_path = os.path.join(os.getcwd(), 'data', 'schema.sql')
    try:
        with open(schema_path, 'r') as f:
            db.executescript(f.read())
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

@app.route('/')
def home():
    return "Welcome to the Budgeting application";

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

