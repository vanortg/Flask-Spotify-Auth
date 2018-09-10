from flask import redirect, jsonify
import base64, json, requests

SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
RESPONSE_TYPE = 'code'   
HEADER = ''
REFRESH_TOKEN = ''
    
def getAuth(client_id, redirect_uri, scope):
    data = "{}client_id={}&response_type=code&redirect_uri={}&scope={}".format(SPOTIFY_URL_AUTH, client_id, redirect_uri, scope) 
    return data

def getToken(code, client_id, client_secret):
    body = {
        "grant_type": "authorization_code",
        "code" : code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }
        
      

    post = requests.post(SPOTIFY_URL_TOKEN, data=body)
     

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

