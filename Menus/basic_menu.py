from api_config import open_link,secret_env,refresh_token
from Flask.flask_config import app
from attempt import see_user


def menu():
    while True:
        print(" 1. Log in ")
        print("2. Menu Trakt")
        
        option=int(input("Select an option : "))
             
        if option == 1:
            client_id,__=secret_env()
            open_link(client_id)
            app.run(port=8000)
            
        if option==2:
            menu_options()
            
            

def menu_options():
    refresh_token()
    see_user()
    

                
                
            
                
                
            
            
        
          
            