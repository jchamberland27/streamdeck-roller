# Stream Deck Roller

## The Plan
The plan for MVP is to take the original Teal 3d dice roller and:

### ToDo
  - [ ] Figure out why gunicorn workers keep dying after a single request.
  - [ ] Come up with a good way to organize a Stream Deck XL dashboard
  - [ ] Come up with a good way to organize a Stream Deck dashboard
  - [ ] Tooling to automate hostname setting within the Stream Deck profiles
  - [ ] Configurable port in build and deploy script.
  - [ ] Push images to some sort of docker repo rather than just building and deploying onsite in the target system.

### Done
  - [x] Serve index.html with a Python Flask app to be accessed from a browser
  - [ ] ~~Strip out the dice selection UI from the HTML~~ Existing UI is still pretty useful for more complex expressions. 
  - [x] Duplicate the original dice UI functionality using API endpoints to build rolling parameters:
    - [x] ADD - adds to the current roll's parameters
    - [x] CLEAR - Deletes the current roll's parameters
    - [x] ROLL - Sends the current roll to the front end to be rendered
    - [x] HOTKEY - assign the last roll to a hotkey value
  - [x] Access the API to control the roller via Stream Deck using the Bar Raiders API ninja plugin: https://docs.barraider.com/faqs/api-ninja/
  - [x] Dockerize the app

## Usage
There's something wrong with gunicorn that is causing the workers to tip over, might be because my linux dev server is so small. Until I figure out what's up with that follow the instructions in the Just Run It section

### Just Run It
Navigate to the src directory, install the dependencies:
```pip3 install -r requirements.txt```
Then just run deckroller.py
```python3 deckroller.py```

### Docker
You should be able to get an image up on port 5000 by running ./docker_build_and_deploy.sh on a system that has a running docker environment. Once the gunicorn stuff is sorted out this will be the recommended way to deploy the service.

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
