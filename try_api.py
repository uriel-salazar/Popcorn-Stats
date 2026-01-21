import os 
from dotenv import load_dotenv 
import requests
import trakt


def prepare_oauth():
    """Loads url for OAuth,the required scopes
    and the neccessary params 

    """
    load_dotenv() 
    url ="https://api.trakt.tv/oauth/authorize"
    scopes =[
        "profile:read",
        "ratings:read",
        "ratings:write",
        "watchlist:read",
        "watchlist:write"
    ]
    params ={"response_type":"code",
            "client_id":os.getenv("client_id"),
            "redirect_uri":"urn:ietf:wg:oauth:2.0:oob"
    }
            
def configure_oauth():
    pass
