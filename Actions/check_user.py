import requests
import json
from OAuth.api_config import secret_env,refresh_token,required_headers

def see_user():
    """
    Greets username with a brief message.
    If the the authorization token doesn't work, it'll open a function 
    for refreshing the token.
    
    """
    url= "https://api.trakt.tv/users/me"
    
    headers=required_headers()
    
    get_info=requests.get(url,headers=headers)
    
    if get_info.status_code == 200:
        info_user = get_info.json()
        print(f" Welcome {info_user} !")
        
    elif get_info.status_code == 400:
        print("Your token has expired")
        refresh_token()
        
def top_movies():
    url_movies="https://api.trakt.tv/movies/popular"
    headers=required_headers()
    requests.get(url_movies,headers=headers)
    

    
    