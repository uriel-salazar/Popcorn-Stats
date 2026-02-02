import requests
import json
from api_config import secret_env,refresh_token

def see_user():
    """
    Greets Trakt username with a brief message.
    If the the authorization token doesn't work, it'll open a function 
    for refreshing the token.
    
    """
    
    with open("tokens.json","r") as credentials:
        
        see_credentials=json.load(credentials)
        access_token=see_credentials["access_token"]
        
    url= "https://api.trakt.tv/users/me"
    client_id,_=secret_env()
    
    headers= {"Content-Type": "application/json",
                "trakt-api-version": "2",
              "trakt-api-key":client_id,
              "Authorization": f"Bearer {access_token}"
    }
    get_info=requests.get(url,headers=headers)
    
    if get_info.status_code == 200:
        info_user = get_info.json()
        print(f" Welcome {info_user} !")
        
    elif get_info.status_code == 400:
        print("Your token has expired")
        refresh_token()
        

    
    