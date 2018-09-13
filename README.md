# Flask-Spotify-Auth 

This extension is for spotify user authentication within a flask app. This flask extension handles user login, scope authentication, access tokens, and refresh cycles for any Spotify registered flask app. Spotify Web API's that have a javascript authentication (i.e. Web Player) can access token information through Jinja3 route calls linking to the getAccessToken method.

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

## Renewal of Access Token and Expiration

Access token renewal is handled automatically by the Flask-Spotify-Auth extension and will update the array returned by getAccessToken() after each expiration period. Renewal can be forced through calls to forceRenewal().

The expiration (in seconds) can be found in the returned array when call getAccessToken(). If error occurs and the access token has not been updated, manually call forceRenewal() and refer to Common Issues for possible solution. Please note that forceRenewal will not return any value, instead a subsequent call must be made to getAccessToken().

## Version Updates

### V0.2

#### Automated Renewal

New to flask-spotify-auth, v0.2 adds automated access token renewal. Clients no longer need to call getAccessToken() after the returned expiration time period. The expiration (in seconds) has been left in the returned array from getAccessToken(), however, calls to the method are unnecessary after the expiration. The field has been left as a returned value for use if error occurs and the access token is not updated. 

#### Routing Changes 

The requirement of a posting callback route has been removed and transitioned to a requirement of one callback route. The callback route can be specified be the client but must be changed within startup.py and must be a listed callback within the Spotify Developers App Dashboard.

#### Jinja Optimization

Flask-Spotify-Auth has been optimized for returning information to jinja calls within JavaScript, or Html files.

## Notes About App Design

If building an app with a Spotify login as the initial startup page, redirecting to the main hompage is best done after sending the returned 'code' to getUserToken(). The Spotify login screen is the only user interaction that this extension requires. 

## Requirements

Requirements for Flask-Spotify-Auth are generally preinstalled in both Flask and Python3, however, for custom installs the following packages are required:

        - Flask:
            -- redirect
            -- requests
        
        - Python3:
            -- json
            -- base64
            -- request
