from dotenv import load_dotenv
from flask import request,Flask
import json,requests,os,webbrowser
from pprint import pprint
from pathlib import Path

app=Flask(__name__)
class UserAuth():
    """ Class for user's authorization.
    """
    def __init__(self):
        app.add_url_rule("/callback",view_func=self.go_back)
    def secret_env(self):
        """
    It gets secret data from .env files by using the library dotenv 
    and the os module.

    Returns:
        client_id (str): Client ID from Trackt API
        client_secret (str): Client Secret from Trackt API
        
    """
        load_dotenv()
        client_id=os.getenv("client_id")
        client_secret=os.getenv("client_secret")
    
        return client_id,client_secret
    
    def open_link(self):
        """
        Opens an url with the required credentials for the 
        authorization code.
        (It opens automatically in your browser)
    
        Returns:
        client_id (str): The client id 
    
        """
        client_id,_ = self.secret_env()
        url = (
        "https://trakt.tv/oauth/authorize"
        f"?response_type=code"
        f"&client_id={client_id}"
        f"&redirect_uri=http://localhost:8000/callback"
        )
    
        webbrowser.open(url)
    
    def go_back(self):
    
        """ Waits for the callback and gets the authorization code
        (Just if the user accepts)
        If there's no authorization code, it will cancel the login.

        """
    # It gets the code if the user accepts the login session. 
        code = request.args.get("code")
        error = request.args.get("error")
        client_id,client_secret = self.secret_env()
    
        if code:
            self.authorization(code,client_id,client_secret)
            return "Successful Authorization"
         
        elif error:
            print("Access denied.")
        
        return "Authorization denied."
    
    def authorization(self,code,client_id,client_secret):
        url="https://trakt.tv/oauth/token"
        payload = {
        "code":code,
        "client_id":client_id,
        "client_secret":client_secret,
        "redirect_uri":"http://localhost:8000/callback",
        "grant_type": "authorization_code" 
        }
    
        headers={"Content-Type":"application/json"}
    
        file=Path("tokens.json")
        if file.exists():
            return
        else:
            try:
                get_access_token=requests.post(url,json=payload,headers=headers,timeout=3)
            
                if get_access_token.status_code == 200:
                    print("Your login was successful!")
                    authorize_json=get_access_token.json()
                    accces=authorize_json["access_token"]
                    refresh=authorize_json["refresh_token"]
                    expire=authorize_json["expires_in"]
                
                tokens={}
                    
                with open("tokens.json","w") as info:
                        tokens["access_token"] = accces
                        tokens["refresh_token"] = refresh
                        tokens["expires_in"] = expire
                        json.dump(tokens,info,indent=4)
                
                           
            except requests.exceptions.ReadTimeout:
                print("Gateway Timeout")
            
            except requests.exceptions.ConnectionError:
                print("Please verify your internet and try again.")
            
        return "Authorization finished."



