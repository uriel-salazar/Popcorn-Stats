from flask import Flask, request
import json
from set_api import secret_env
from ouath import authorization
app = Flask(__name__) 


@app.route("/callback")
def callback():
    
    """ Waits for the callback and gets the authorization code
    (Just if the user accepts)
    If there's no authorization code, 

    """
    # Gets the code if the user accepts the log in session. 
    code = request.args.get("code")
    error=request.args.get("error")
    client_id,client_secret =secret_env()
    
    if code:
        authorization(code,client_id,client_secret)
         
    elif error:
        
        return "Authorization denied."
    
    return "Finished."
    


def show_strange_code(get_token):
    see_json=get_token.json()
    print(see_json)
    accces=see_json["access_token"]
    refresh=see_json["refresh_token"]
    expire=see_json["expires_in"]    
    with open("credentials.json","r") as file:
        data =json.load(file)
        data["access_token"] = accces
        data["refresh_token"] = refresh
        data["expires_in"]= expire
        
        
    with open("credentials.json","w") as info:
        json.dump(data,info,indent=4) 
    return "Got it "





    
    
    