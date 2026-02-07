import os
from dotenv import load_dotenv
import requests,json
from OAuth.api_config import *


def secret_env():
    """
    Gets secret data from .env files by using  the library dotenv 
    and the os module.

    Returns:
        client_id (str): Client ID from Trackt API
        client_secret (str): Client secret from Trackt API
        
    """
    load_dotenv()
    client_id=os.getenv("client_id")
    client_secret=os.getenv("client_secret")
    
    return client_id,client_secret


    
def refresh_token():
    """ Rewrites the old access and refresh token for a new one in the file.
    If the file doesn't exist yet, it'll exit this function with a return. 
    
    """
    client_id,client_secret = secret_env()
    url = "https://trakt.tv/oauth/token"
    with open("tokens.json", "r") as f:
        old_token = json.load(f)

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": old_token["refresh_token"],
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": "http://localhost:8000/callback"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers,timeout=3)

        if response.status_code == 200:
            new_data = response.json()
            # It replaces the old tokens with the new ones
            old_token["access_token"] = new_data["access_token"]
            old_token["refresh_token"] = new_data["refresh_token"]

            with open("tokens.json", "w") as change_token:
                json.dump(old_token, change_token, indent=4)
       
        elif response.status_code != 200:
            print("Error",response.status_code,response.text)
    
    except requests.exceptions.ConnectionError:
        print(" Bad Internet Connection")
        
    # If the timeout ends, it throws this exception
    except requests.exceptions.ReadTimeout:
       print("Gateway Timeout 🌐❌")


def file_exist():
    
    if os.path.exists("tokens.json"):
        file=True
    else:
        file = False
    return file

def required_headers():
    """ Automates the default headers for TraktAPI.

    Returns:
        (dict): The required headers for API calls. 
    """
    
    with open("tokens.json","r") as credentials:
        
        see_credentials=json.load(credentials)
        access_token=see_credentials["access_token"]
        
    client_id,_=secret_env()
    
    return {"Content-Type": "application/json",
                "trakt-api-version": "2",
              "trakt-api-key":client_id,
              "Authorization": f"Bearer {access_token}"
    }


    

        
    
    
    
    
    
        

    
    
        
        
    
        
        
    
    

