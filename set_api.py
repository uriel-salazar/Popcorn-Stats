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
        catch_token=requests.post(url,json=body,headers=headers)
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
                    refresh_token(client_id,client_secret)
                    
                    
    except requests.exceptions.ConnectionError:
        print("Error Internet.")
    
    
def refresh_token(client_id,client_secret):

    url = "https://api.trakt.tv/oauth/token"
    
    with open("credentials.json","r") as see:
        see_credentials=json.load(see)
        refresh_token=see_credentials["refresh_token"]
        

    payload ={
  "refresh_token": refresh_token,
  "client_id": client_id,
  "client_secret": client_secret,
  "redirect_uri": "http://localhost:8000/callback",
  "grant_type": "refresh_token"
}
    headers={"Content-Type":"application/json"}
    get_new_code=requests.post(url,json=payload,headers=headers)
    
    if get_new_code.status_code==200:
        print("Sucesss you got a new code")
        see_new_json=get_new_code.json()
        print(see_new_json) # New json with the new access token 
    
    elif get_new_code.status_code!=200:
        print(f"Unsuccessful,{get_new_code.status_code}")
    
 
    
    
    
    
    
    
        

    
    
        
        
    
        
        
    
    

