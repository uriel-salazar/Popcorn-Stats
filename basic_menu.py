from set_api import authorize_code
from flask_config import app
from set_api import secret


def menu():
    while True:
        print(""" 1. Initialize OAuth
              2. Something Else""")
        
        option=int(input("Select an option : "))
        if option==1:
            client_id,client_secret=secret()
            authorize_code(client_id)
            app.run(port=8000)
          
            