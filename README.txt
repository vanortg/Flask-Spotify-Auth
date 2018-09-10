# Flask Spotify Authentication
Simple flask backend to handle authorization and renewal of spotify users acess token

# Initial Setup (for example routes configuration see app.py):
      @app.route('/'): 
          -must call startup.getUser() and redirect the response for spotify verification
      @app.route(YOUR CALLBACK LOCATION):
          -must include startup.getUserToken(request.args['code']) and redirect to your main html page
 
# Startup.py Setup:
      - Add your registered apps client_id and client_secret.
      - Change the callback and port location (DEFAULT LOCATION: localhost:5000)
