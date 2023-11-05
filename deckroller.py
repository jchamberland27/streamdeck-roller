#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO
import notation
import json

app = Flask(__name__)
socketio = SocketIO(app)
current_roll = []

@app.route('/')
def display_ui():
    """Display the UI for the Deck Roller."""
    return render_template('index.html')

@app.route('/add')
def add():
    """Add to the current roll"""
    #TODO Validate the input
    global current_roll
    current_roll.extend(notation.dice_notation_to_list(request.args.get('add')))
    return 'ADD OK'

@app.route('/clear')
def clear():
    """Clear the current roll"""
    global current_roll
    current_roll = []
    return 'CLEAR OK'

@app.route('/roll')
def roll():
    """Roll the current roll"""
    global current_roll
    socketio.emit('roll', json.dumps(notation.prepare_roll(current_roll)))
    return 'ROLL OK'

#Start app
if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
