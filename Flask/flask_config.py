from flask import Flask, request
import json
from OAuth.api_config import secret_env
from OAuth.ouath import authorization
app = Flask(__name__) 


@app.route("/callback")
def callback():
    
    """ Waits for the callback and gets the authorization code
    (Just if the user accepts)
    If there's no authorization code, it will cancel the login.

    """
    # It gets the code if the user accepts the login session. 
    code = request.args.get("code")
    error = request.args.get("error")
    client_id,client_secret =secret_env()
    
    if code:
        got_access=authorization(code,client_id,client_secret)
         
    elif error:
        print("Access denied.")
        
        return "Authorization denied."
    
    return "Successful Authorization"

    







    
    
    