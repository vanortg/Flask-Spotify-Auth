from flask_spotify_auth import getAuth, refreshAuth, getToken

#Add your client ID
# YOU SHOULD USE os.environ['CLIENT']
CLIENT_ID = "98c167e218bd483891f8638caaca19cb"

#aDD YOUR CLIENT SECRET FROM SPOTIFY
# YOU SHOULD USE os.environ['SECRET']
CLIENT_SECRET = "e40d06af72524208bf0bbb048ba299a3"

#Port and callback url can be changed or ledt to localhost:5000
PORT = "5000"
CALLBACK_URL = "http://localhost"

#Add needed scope from spotify user
SCOPE = "streaming user-read-birthdate user-read-email user-read-private"
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, "{}:{}/callback/".format(CALLBACK_URL, PORT), SCOPE)

def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))

def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()

def getAccessToken():
    return TOKEN_DATA
