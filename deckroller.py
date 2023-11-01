#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
current_roll = ''

@app.route('/')
def display_ui():
    """Display the UI for the Deck Roller."""
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    """Add to the current roll"""
    #TODO Validate the input
    global current_roll
    current_roll += request.form['add']
    return 'ADD OK'

@app.route('/clear', methods=['POST'])
def clear():
    """Clear the current roll"""
    global current_roll
    current_roll = ''
    return 'CLEAR OK'

@app.route('/roll', methods=['POST'])
def roll():
    """Roll the current roll"""
    global current_roll
    #TODO Tell the client to roll
    return 'ROLL OK'

#Start app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
