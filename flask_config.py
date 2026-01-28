from flask import Flask, request
import json
app = Flask(__name__) 

@app.route("/callback")
def callback():
    """ Waits for the callback and gets the authorization code
    (Just if the user accepts)
    If there's no authorization code, 

    """
    code = request.args.get("code")
    error=request.args.get("error")
    
    if code:

        with open("credentials.json", "r") as c:
             data = json.load(c)

        if data.get("authorization_code") is None:
            data["authorization_code"] = code

            with open("credentials.json", "w") as c:
                json.dump(data, c, indent=4)
    
    #If the authorization is denied :
    elif error:
        
        return "Authorization denied."
    
    return "Authorization finished." 




    
    
    