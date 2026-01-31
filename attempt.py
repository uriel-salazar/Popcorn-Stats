import requests
import json
from api_config import secret_env

def see_user():
    
    url= "https://api.trakt.tv/users/me"
    client_id,_=secret_env()
    
    headers= {"Content-Type": "application/json",
                "trakt-api-version": "2",
              "trakt-api-key":client_id,
              "Authorization": "Bearer a1d8eb77676a0a54456bd42f444b323e49ccc3c3de96eff7aeaea1210b24520f "
    }
    get_info=requests.get(url,headers=headers)
    
    if get_info.status_code == 200:
        print("Sucesss")
        see=get_info.json()
        print(see)
        unauthorized= False
    elif get_info.status_code == 401:
        print("You're unauthorized")
        unauthorized=True
    return unauthorized

    
    