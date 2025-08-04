# main.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator!"

@app.route('/add')
def add():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return f"Result: {a + b}"
    except:
        return "Error: Invalid input"

if __name__ == '__main__':
    app.run()
