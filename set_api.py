import os
from dotenv import load_dotenv
import webbrowser
import requests
import json
from pprint import pprint
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

    
def get_code():
    
    with open("credentials.json","r") as see_codes:
        info=json.load(see_codes)
        authorization_code=info["authorization_code"]
    return authorization_code

def accces_token(client_secret,client_id,authorization_code):
    """ Catches the access token when the user accepts authorization
    Reads and writes a file json (Where the auth codes are contained) for saving the access token.
    A block of a try and except for managing the lack of Internet. 
    
    

    Args:
        client_secret (str): My client secret from Trakt API
        client_id (str): My client id from Trakt API 
        authorization_code (str): _description_
    """
    
    url="https://trakt.tv/oauth/token"
    body={
  "code":authorization_code,
  "client_id":client_id,
  "client_secret":client_secret,
  "redirect_uri":"http://localhost:8000/callback",
  "grant_type": "authorization_code" 
}
    headers={"Content-Type":"application/json"}
    
    
    try:
        catch_token=requests.post(url,json=body,headers=headers,timeout=2)
        see_json=catch_token.json()
    
        if catch_token.status_code==200:
            print("Success")
            pprint(see_json)

            accces=see_json["access_token"]
            refresh=see_json["refresh_token"] #test
            
            with open("credentials.json","r") as file:
                data=json.load(file)
                data["access_token"]=accces
                data["refresh_token"]=refresh #test 
        
                with open("credentials.json","w") as info:
                    json.dump(data,info,indent=4)
        
            
        # tiny draft 
        elif catch_token.status_code==400: ## track 
                    refresh_token(client_id,client_secret,url)
                    
                    
    except requests.exceptions.ConnectionError:
        print("Error Internet.")
        
    except requests.exceptions.ConnectTimeout:
        print("Timeout Error. ")
        

        
    
    
def refresh_token(client_id, client_secret,url):
    """ Rewrites the old access and refresh token for a new one in the file.
    
    Args:
        client_id (str): Client id from Trakt API.
        client_secret (str): Client secret from Trakt API.
        url (str): The url for getting the new token.
    """
    
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
    
        
    
    
    
    
    
        

    
    
        
        
    
        
        
    
    

