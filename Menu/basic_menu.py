from api_config import open_link,secret_env
from Flask.flask_config import app



def menu():
    while True:
        print(""" 1. Log in 
              2. Something Else""")
        
        option=int(input("Select an option : "))
        if option==1:
            client_id,client_secret=secret_env()
            open_link(client_id)
            app.run(port=8000)
          
            