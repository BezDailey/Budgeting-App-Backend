from flask import Flask, request

app = Flask(__name__)

users = {'jabezdailey@icloud.com': 'password'}

def auth(email, password):
    if email in users and password == users[email]:
        return True
    else:
        return False

@app.route('/')
def home():
    return "Welcome to the Budgeting application"

@app.route('/login', methods=['POST']) 
def login():
    email = request.form['email']
    password = request.form['password']

    if auth(email, password):
        return "successful login!"
    else:
        return "Incorrect password or email."

@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    users[email] = password
    return "User created successfully!"

if __name__ == '__main__':
    app.run(debug=True)
