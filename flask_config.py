from flask import Flask, request
import json
import os
from dotenv import load_dotenv

import requests
app = Flask(__name__) 





@app.route("/callback")
def callback():
    load_dotenv()
    """ Waits for the callback and gets the authorization code
    (Just if the user accepts)
    If there's no authorization code, 

    """
    code = request.args.get("code")
    error=request.args.get("error")
    
    client_secret=os.getenv("client_secret")
    client_id=os.getenv("client_id")
    
    if code:

        url="https://trakt.tv/oauth/token"
    
        payload = {
        "code":code,
        "client_id":client_id,
        "client_secret":client_secret,
        "redirect_uri":"http://localhost:8000/callback",
    "grant_type": "authorization_code" 
    }
    
        headers={"Content-Type":"application/json"}
    
        get_access_token=requests.post(url,json=payload,headers=headers,timeout=3)
        
        if get_access_token.status_code == 200:
            print(f'Success')
            see_token=get_access_token.json
            print(see_token)
            
        elif get_access_token.status_code !=200:
            print(get_access_token.text)
    
    elif error:
        
        return "Authorization denied."
    
    
    return "Authorization finished." 




    
    
    