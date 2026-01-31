import requests
import json
from pprint import pprint
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
                
                with open("credentials.json","r") as file:
                    data=json.load(file)
                    data["access_token"] = accces
                    data["refresh_token"] = refresh
                    data["expires_in"] = expire
        
                with open("credentials.json","w") as info:
                    json.dump(data,info,indent=4)
            
            elif get_access_token.status_code == 400:
                    print("Error, you might need a refresh token")
                 
    except requests.exceptions.ConnectTimeout:
            print("Connection Timeout,please try again")
            
    except requests.exceptions.ConnectionError:
            print("Please verify your internet and try again.")
            
    return "Authorization finished."
