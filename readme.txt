Stream Deck Roller
==================
The plan is to take the original Teal 3d dice roller and:
  - Serve index.html with a Python Flask app to be accessed from a browser
  - Strip out the dice selection UI from the HTML
  - Duplicate the original dice UI functionality using API endpoints to build rolling parameters:
    - ADD - adds to the current roll's parameters
    - CLEAR - Deletes the current roll's parameters
    - ROLL - Sends the current roll to the front end to be rendered
  - Access the API to control the roller via Stream Deck using the Bar Raiders API ninja plugin:
    - https://docs.barraider.com/faqs/api-ninja/


Original Readme
===============
Teal 3d dice sources.
To run open dice/index.html with your browser.
Can be used stand-alone.
dice.py is a GAE serverlet that makes proxy requests to random.org API.


This is originally taken from
http://www.teall.info/2014/01/online-3d-dice-roller.html, then
refactored and imported to GitHub.

License is MIT, authors Anton Natarov (original code) and Esteban
Manchado Velázquez (refactoring and small improvements).
