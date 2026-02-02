from api_config import open_link,secret_env,file_exist
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
    file=file_exist()
    if file:
        while True:
            print("1. See your user")
            print("2.")
            print("3.")
            choose_action=int(input("Please, select an option :"))
        
            if choose_action==1:
                see_user()
    else:
        print("You can't have access to this actions.")
        print("You must authorize your account.")
            
    

                
                
            
                
                
            
            
        
          
            