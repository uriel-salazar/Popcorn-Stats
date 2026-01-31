from api_config import open_link,secret_env
from Flask.flask_config import app
from attempt import see_user


def menu():
    while True:
        print(" 1. Log in ")
        print("2. Did you already log in??")
        print("3. Check profile")
        
        option=int(input("Select an option : "))
             
        if option == 1:
            client_id,client_secret=secret_env()
            open_link(client_id)
            app.run(port=8000)
        if option == 2:
            unauthorized=see_user()
            if unauthorized == True:
                
                
            
            
        
          
            