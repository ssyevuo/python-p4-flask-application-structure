#!/usr/bin/env python3

from flask import Flask

# helps file figure out where the application is and where its important files will be
app = Flask(__name__)

# defining routes
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# development server
if __name__ == '__main__':
    app.run(port=5555, debug=True)
