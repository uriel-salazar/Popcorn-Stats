import os
from dotenv import load_dotenv
import webbrowser
import requests
import json

def secret():
    """
    Retrieves secret data from .env files by using load_dotenv()
    and os 

    Returns:
        client_id (str): Client ID from Trackt API
        client_secret (str): Client secret from Trackt API
        
    """
    load_dotenv()
    client_id=os.getenv("client_id")
    client_secret=os.getenv("client_secret")
    
    return client_id,client_secret

def authorize_code(client_id):
    """
    It sets up the url link with the required credentials for the 
    authorization code.
    And opens the link automatically.
    
    Returns:
        client_id (str): The client id 
    
    """
    url = (
        "https://trakt.tv/oauth/authorize"
        f"?response_type=code"
        f"&client_id={client_id}"
        f"&redirect_uri=http://localhost:8000/callback"
    )
    
    
    webbrowser.open(url)
    return client_id

    
        

    
def refresh_token(client_id, client_secret):
    """ Rewrites the old access and refresh token for a new one in the file.
    
    Args:
        client_id (str): Client id from Trakt API.
        client_secret (str): Client secret from Trakt API.
        url (str): The url for getting the new token.
    """
    
    url = "https://trakt.tv/oauth/token"
    with open("credentials.json", "r") as f:
        tokens= json.load(f)

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": tokens["refresh_token"],
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
            print("Success, new token ")
            new_data = response.json()
            # It replaces the old token with the new one 
            new_data["access_token"] =tokens["access_token"]
            new_data["refresh_token"] = tokens["refresh_token"]

            with open("credentials.json", "w") as f:
                json.dump(tokens, f, indent=4)
        # If the response is not successful, it throws an error
        elif response.status_code !=200:
            print("Error",response.status_code)
    
    except requests.exceptions.ConnectionError:
        print(" Bad Internet Connection")
        
    # If the timeout ends, it throws this exception
    except requests.exceptions.ConnectTimeout:
       print("")
    
        
    
    
    
    
    
        

    
    
        
        
    
        
        
    
    

