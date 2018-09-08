from flask import requests
import base64, json

SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
RESPONSE_TYPE = 'code'   
HEADER = ''
REFRESH_TOKEN = ''
    
def getAuth(client_id, client_secret, redirect_uri, scope):
    data = requests.get('{}client_id={}&response_type={}&redirect_uri={}&scope={}'.format(SPOTIFY_URL_AUTH, client_id, response_type, redirect_uri, scope))
  
    body = {
        "grant_type": "authorization_code",
        "code" : str(data.code),
        "redirect_uri": redirect_uri
    }
    
    HEADER = {"Authorization" : "Basic {}".format(base64.b64encode("{}:{}".format(client_id, client_secret)))} 

    post = requests.post(SPOTIFY_URL_TOKEN, data=body, headers=HEADER)

    response = json.loads(post.text)

    auth_head = {"Authorization": "Bearer {}".format(response["access_token"])}
    REFRESH_TOKEN = response["refresh_token"]
    return [auth_head, response["scope"], response["expires_in"]]

def refreshAuth():
    body = {
        "grant_type" : "refresh_token",
        "refresh_token" : REFRESH_TOKEN
    }

    post_refresh = requests.post(SPOTIFY_URL_TOKEN, data=body, headers=HEADER)
    post_response = json.loads(post_refresh.text)
    
    auth_head = {"Authorization": "Bearer {}".format(post_response["access_token"])}
    return [auth_head, post_response["scope"], response["expires_in"]]

