import os
from dotenv import load_dotenv
import webbrowser


def authorize_code():
    """
    Initializes my client id  from the env. file, and executes an url 
    for the authorization code. 
    
    """
    load_dotenv()
    client_id = os.getenv("client_id")

    url = (
        "https://trakt.tv/oauth/authorize"
        f"?response_type=code"
        f"&client_id={client_id}"
        f"&redirect_uri=http://localhost:8000/callback"
    )
    
    webbrowser.open(url)

    
        
        
    
        
        
    
    

