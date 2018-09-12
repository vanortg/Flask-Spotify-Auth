# Flask Spotify Auth 

This repo is for spotify user authentication within a flask app. This flask extension handles user login, scope authentication, access tokens, and refresh cycles for any Spotify registered flask app. Spotify Web API's that have a javascript authentication (i.e. Web Player) can access token information through Jinja3 route calls linking to the getAccessToken method.

## Initial Setup

NOTE: Flask Spotify Auth is built for Python3

Implementing this flask extension requires the Client ID, Client Secret, and a registered callback found within the Spotify Developer Dashboard. By default the callback links to http://localhost:5000/callback/. Registering a different callback must be done within the Spotify Dashboard and changed within the authentication process listed below.

### Adding Client ID and Client Secret

startup.py is the only file needing modification. Within startup.py you must enter your Client ID, Client Secret, Callback, and Port into the corresponding variables. The callback and Port by default are listed as localhost and 5000. If left default the callback url, http://localhost:5000/callback/ must be registered as a redirect uri within the Spotify Developer Dashboard.

### Required Routing

The Flask-Spotify-Auth extension reqiures specific routing to allow redirecting to the Spotify Authentication page for scope authentication.

#### Redirecting to Spotify Login

To cause the initial redirect for Spotify user authentication the startup.py method getUser() must be called with its response being a redirect returned to the flask app page. For example, an app that gets the users authentication before initial startup will look as follows: 

            from flask import Flask, redirect
            import startup
            
            @app.route('/')
            def index():
                response = startup.getUser()
                return redirect(response)

#### Recieving the Spotify Authentication

Information will then be passed back through the redirect uri specified within the Spotify Developer App Dashboard. The redirect route must then pass the recieved 'code' value to the getUserToken() method within startup.py. An example of this setup with the redirect uri as http://localhost:5000/callback/ will look as follows:

            from flask import Flask, redirect, request
            import startup

            @app.route('/')
            def index():
                response = startup.getUser()
                return redirect(response)
            
            @app.route('/callback/')
                startup.getUserToken(request.args['code'])
                ** I redirect to my homepage here **

After passing the recieved code back to flask-spotify-auth the access token needed for all calls to Spotify API's will be available.

### Getting the Access Token

The access token, returned in an array with the required authentication header, authorized scopes, and expiration time (in seconds), can be accessed through the getAccessToken() within startup.py. Calling this method will return an array in the following format:

    [ACCESS_TOKEN, AUTHENTICATION_HEADER, AUTHORIZED_SCOPES, EXPIRATION]

