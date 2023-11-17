# Stream Deck Roller

## Installation
Recommended way to run is with Docker

### Docker
You should be able to get an image up on port 5000 by running ```./docker_build_and_deploy.sh``` in the docker directory on a system that has a running docker environment.

### Just Run It
Navigate to the src directory, install the dependencies:

```pip3 install -r requirements.txt```

Then just run deckroller.py with gunicorn

```gunicorn -b 0.0.0.0:5000 --worker-class eventlet -w 1 deckroller:app```

## Usage

### Via UI
Navigate to the ip and port your service is running on in a browser to display the UI. You should be able to use the roller as originally designed through the UI.

### Streamdeck
TODO

## Roadmap
The plan for MVP is to take the original Teal 3d dice roller and:

### ToDo
  - [ ] Come up with a good way to organize a Stream Deck XL dashboard
  - [ ] Come up with a good way to organize a Stream Deck dashboard
  - [ ] Tooling to automate hostname setting within the Stream Deck profiles
  - [ ] Configurable port in build and deploy script.
  - [ ] Push images to some sort of docker repo rather than just building and deploying onsite in the target system.

### Done
  - [x] Figure out why gunicorn workers keep dying after a single request.
  - [x] Serve index.html with a Python Flask app to be accessed from a browser
  - [ ] ~~Strip out the dice selection UI from the HTML~~ Existing UI is still pretty useful for more complex expressions. 
  - [x] Duplicate the original dice UI functionality using API endpoints to build rolling parameters:
    - [x] ADD - adds to the current roll's parameters
    - [x] CLEAR - Deletes the current roll's parameters
    - [x] ROLL - Sends the current roll to the front end to be rendered
    - [x] HOTKEY - assign the last roll to a hotkey value
  - [x] Access the API to control the roller via Stream Deck using the Bar Raiders API ninja plugin: https://docs.barraider.com/faqs/api-ninja/
  - [x] Dockerize the app


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
