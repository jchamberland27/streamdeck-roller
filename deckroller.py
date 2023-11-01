#!/usr/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def display_ui():
    """Display the UI for the Deck Roller."""
    return render_template('index.html')

#Start app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
