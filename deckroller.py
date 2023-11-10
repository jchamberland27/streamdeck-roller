#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO
import notation
import json

app = Flask(__name__)
socketio = SocketIO(app)
current_roll = []
last_roll = []
hotkey_rolls = {}
hotkey_set = False


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
    global current_roll, hotkey_set
    current_roll = []
    hotkey_set = False
    return 'CLEAR OK'


@app.route('/hotkey')
def hotkey():
    global hotkey_rolls, last_roll
    """roll a saved hotkey roll"""
    if request.args.get('hotkey') not in hotkey_rolls.keys() and hotkey_set == False:
        return 'HOTKEY UNASSIGNED', 401
    elif hotkey_set == True:
        hotkey_rolls[request.args.get('hotkey')] = last_roll
        hotkey_set = False
        return 'HOTKEY OK'
    else:
        socketio.emit('roll', json.dumps(notation.prepare_roll(hotkey_rolls[request.args.get('hotkey')])))
        last_roll = hotkey_rolls[request.args.get('hotkey')]
        return 'HOTKEY OK'
        

@app.route('/last')
def last():
    """Roll the last roll"""
    global last_roll
    socketio.emit('roll', json.dumps(notation.prepare_roll(last_roll)))
    return 'LAST OK'


@app.route('/roll')
def roll():
    """Roll the current roll"""
    global current_roll, last_roll
    socketio.emit('roll', json.dumps(notation.prepare_roll(current_roll)))
    last_roll = current_roll
    current_roll = []
    return 'ROLL OK'


@app.route('/set_hotkey')
def set_hotkey():
    """Assign the last roll to a hotkey"""
    global hotkey_set
    if hotkey_set == False:
        hotkey_set = True
    else:
        hotkey_set = False
    return 'HOTKEY_SET OK'

#Start app
if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
