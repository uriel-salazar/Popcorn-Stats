import requests,json
from OAuth.api_config import refresh_token,required_headers
from pprint import pprint

def check_user():
    """
    Greets username with a brief message.
    If the the authorization token doesn't work, it'll open a function 
    for refreshing the token.
    
    """
    url= "https://api.trakt.tv/users/me"
    
    headers=required_headers()
    
    get_user=requests.get(url,headers=headers,timeout=3)
    
    if get_user.status_code == 200:
        info_user = get_user.json()
        print(f" Welcome {info_user} !")
        
    elif get_user.status_code == 401:
        refresh_token()
        
def top_movies():
    
    url_movies="https://api.trakt.tv/movies/popular"
    headers=required_headers()
    try:
        get_top=requests.get(url_movies,headers=headers,timeout=3)
        if get_top.status_code == 200:
            movies_json = get_top.json()
        
        elif get_top.status_code ==401:
            refresh_token()
            
    except requests.exceptions.ConnectTimeout:
        print("Gateway Timeout")
    
    except requests.exceptions.ConnectionError:
        print("Check your Connection ⚠️")
    return movies_json

def top_show():
    url_show="https://api.trakt.tv/shows/popular"
    headers=required_headers()
    try:
        get_top_show=requests.get(url_show,headers=headers,timeout=3)
        
        if get_top_show.status_code==200:
            print("Success")
            movies_json=get_top_show.json()
            pprint(movies_json)
        
        elif get_top_show==401:
             refresh_token()
    
    except requests.exceptions.ConnectTimeout:
         print("Gateway Timeout")
         
    except requests.exceptions.ConnectionError:
        print("Check your Connection ⚠️")
        
            
    
    
    

    
    