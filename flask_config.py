from flask import Flask, request
import json
from set_api import secret_env
from set_api import refresh_token
import requests
app = Flask(__name__) 



@app.route("/callback")
def callback():
    
    """ Waits for the callback and gets the authorization code
    (Just if the user accepts)
    If there's no authorization code, 

    """
    # Gets the code if the user accepts the log in session. 
    code = request.args.get("code")
    error=request.args.get("error")
    client_id,client_secret =secret_env()
    
    
    if code:
        url="https://trakt.tv/oauth/token"
        
        with open("credentials.json","r") as available:
            n=json.load(available,client_id,client_secret)

        access_token=n["access_token"]
        if access_token is None:
            authorization(code)
        else:
            print("nop")
            
        payload = {
        "code":code,
        "client_id":client_id,
        "client_secret":client_secret,
        "redirect_uri":"http://localhost:8000/callback",
    "grant_type": "authorization_code" 
    }
    
        headers={"Content-Type":"application/json"}
        
        try:
            get_access_token=requests.post(url,json=payload,headers=headers,timeout=3)
            if get_access_token.status_code == 200:
                return show_strange_code(get_access_token)
            
            elif get_access_token.status_code == 400:
                refresh_token(client_secret,client_id)
                
            
        except requests.exceptions.ConnectTimeout:
            print("Connection Timeout,please try again")
            
        except requests.exceptions.ConnectionError:
            print("Please verify your internet and try again.")

    elif error:
        
        return "Authorization denied."
    
    return "Authorization finished."


def show_strange_code(get_token):
    see_json=get_token.json()
    print(see_json)
    accces=see_json["access_token"]
    refresh=see_json["refresh_token"]
    expire=see_json["expires_in"]    
    with open("credentials.json","r") as file:
        data =json.load(file)
        data["access_token"] = accces
        data["refresh_token"] = refresh
        data["expires_in"]= expire
        
        
    with open("credentials.json","w") as info:
        json.dump(data,info,indent=4) 
    return "Got it "


def authorization(code,client_id,client_secret):
    url="https://trakt.tv/oauth/token"
    
    payload = {
        "code":code,
        "client_id":client_id,
        "client_secret":client_secret,
        "redirect_uri":"http://localhost:8000/callback",
    "grant_type": "authorization_code" 
    }
    
    headers={"Content-Type":"application/json"}
        
    try:
            get_access_token=requests.post(url,json=payload,headers=headers,timeout=3)
            if get_access_token.status_code == 200:
                return show_strange_code(get_access_token)
            
            elif get_access_token.status_code == 400:
                refresh_token(client_secret,client_id)
                
            
    except requests.exceptions.ConnectTimeout:
            print("Connection Timeout,please try again")
            
    except requests.exceptions.ConnectionError:
            print("Please verify your internet and try again.")

    



    
    
    