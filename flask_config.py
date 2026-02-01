from flask import Flask, request
import json
from api_config import secret_env
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
    

@app.get("/shutdown")
def shutdown():
    app.s



    
    
    