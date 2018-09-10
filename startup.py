from flask_spotify_auth import getAuth, refreshAuth, getToken

#Add your client ID
CLIENT_ID = ""

#aDD YOUR CLIENT SECRET FROM SPOTIFY
CLIENT_SECRET = ""

#Port and callback url can be changed or ledt to localhost:5000
PORT = "5000"
CALLBACK_URL = "http://localhost"

#Add needed scope from spotify user
SCOPE = ""
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown 
TOKEN_DATA = []

def getUser():
    return getAuth(CLIENT_ID, "{}:{}/callback/".format(CALLBACK_URL, PORT), SCOPE)

def getUserToken(code):
    tokenData = getToken(code, CLIENT_ID, CLIENT_SECRET)
 
def refreshToken(time):
    time.sleep(time)
    tokenData = refreshAuth()
