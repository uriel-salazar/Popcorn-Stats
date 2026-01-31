from set_api import authorize_code,secret_env
from flask_config import app



def menu():
    while True:
        print(""" 1. Log in 
              2. Something Else""")
        
        option=int(input("Select an option : "))
        if option==1:
            client_id,client_secret=secret_env()
            authorize_code(client_id)
            app.run(port=8000)
          
            