from flask import Flask, request

app = Flask(__name__) 

@app.route("/callback")
def callback():
    """ Waits for the callback and gets the authorization code 

    """
    code = request.args.get("code")
    with open("auth_code.txt","w") as c:
        c.write(code)
    return "Success"




    
    
    