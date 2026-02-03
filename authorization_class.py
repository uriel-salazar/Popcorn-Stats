from dotenv import load_dotenv
import os
import webbrowser
from Flask.flask_config import app
from flask import request

class UserActions():
    def __init__(self):
        pass
    def secret_env(self):
        """
    Retrieves secret data from .env files by using  the library dotenv 
    and the os module.

    Returns:
        client_id (str): Client ID from Trackt API
        client_secret (str): Client secret from Trackt API
        
    """
        load_dotenv()
        client_id=os.getenv("client_id")
        client_secret=os.getenv("client_secret")
        print(client_id)
    
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
        return client_id

    @app.route("/callback")
    def callback(self):
    
        """ Waits for the callback and gets the authorization code
        (Just if the user accepts)
        If there's no authorization code, it will cancel the login.

        """
    # It gets the code if the user accepts the login session. 
        code = request.args.get("code")
        error = request.args.get("error")
        client_id,client_secret = self.secret_env()
    
        if code:
            got_access=self.authorization(code,client_id,client_secret)
            return "Successful Authorization"
         
        elif error:
            print("Access denied.")
        
        return "Authorization denied."

user1=UserActions()

user1.secret_env()
user1.open_link()
