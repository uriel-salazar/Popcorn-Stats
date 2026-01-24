from flask import Flask, request

app = Flask(__name__) 

@app.route("/callback")
def callback():
    """ Waits for the callback and gets the authorization code 

    """
    code = request.args.get("code")
    print("CODE:", code) # The authorization code 
    return "Success"


if __name__ == "__main__":
    app.run(port=8000) #it'll run in  8000 port 
    

    
    
    