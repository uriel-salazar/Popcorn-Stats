import os 
from dotenv import load_dotenv 
import requests
import trakt
import webbrowser 


def sign_in(): 
    load_dotenv()
    url="https://trakt.tv/oauth/authorize"
    
    params ={"response_type":"code",
            "redirect_uri":"urn:ietf:wg:oauth:2.0:oob"
    }
    try:
        b=requests.get(url,params=params,timeout=2)
        if b.status_code==200:
           webbrowser.open(b.url)
        else:
            print("Erorr:",b.status_code())
    except requests.exceptions.Timeout:
        print("Timeout Error")
        
        
    
        
        
    
    

