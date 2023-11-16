# Stream Deck Roller

## The Plan
The plan for MVP is to take the original Teal 3d dice roller and:
### ToDo
  - [ ] Come up with a good way to organize a Stream Deck XL dashboard
  - [ ] Come up with a good way to organize a Stream Deck dashboard
  - [ ] Dockerize the app
  - [ ] Tooling to automate hostname setting within the profiles

### Done
  - [x] Serve index.html with a Python Flask app to be accessed from a browser
  - [ ] ~~Strip out the dice selection UI from the HTML~~ Existing UI is still pretty useful for more complex expressions. 
  - [x] Duplicate the original dice UI functionality using API endpoints to build rolling parameters:
    - [x] ADD - adds to the current roll's parameters
    - [x] CLEAR - Deletes the current roll's parameters
    - [x] ROLL - Sends the current roll to the front end to be rendered
    - [x] HOTKEY - assign the last roll to a hotkey value
  - [x] Access the API to control the roller via Stream Deck using the Bar Raiders API ninja plugin: https://docs.barraider.com/faqs/api-ninja/

## Usage
- TODO

# Original Pre-Fork Readme
Teal 3d dice sources.
To run open dice/index.html with your browser.
Can be used stand-alone.
dice.py is a GAE serverlet that makes proxy requests to random.org API.


This is originally taken from
http://www.teall.info/2014/01/online-3d-dice-roller.html, then
refactored and imported to GitHub.

License is MIT, authors Anton Natarov (original code) and Esteban
Manchado Velázquez (refactoring and small improvements).
