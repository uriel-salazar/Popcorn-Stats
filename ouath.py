import requests

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
