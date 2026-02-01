import requests
import json
from pprint import pprint
from pathlib import Path
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
                print("You finally got your access token")
                authorize_json=get_access_token.json()
                pprint(authorize_json)
                accces=authorize_json["access_token"]
                refresh=authorize_json["refresh_token"]
                expire=authorize_json["expires_in"]#test
                
                file=Path("tokens.json")
                if file.exists():
                    return
                else:
                    tokens={}
                    
                    with open("tokens.json","w") as info:
                        tokens["access_token"] = accces
                        tokens["refresh_token"] = refresh
                        tokens["expires_in"] = expire
                        json.dump(tokens,info,indent=4)
                
                
                 
    except requests.exceptions.ConnectTimeout:
            print("Connection Timeout,please try again")
            
    except requests.exceptions.ConnectionError:
            print("Please verify your internet and try again.")
            
    return "Authorization finished."
