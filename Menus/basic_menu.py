from OAuth.api_config import open_link,secret_env,file_exist
from Flask.flask_config import app
from check_user import see_user
from Validate.validate_input import verify_number


def menu():
    """ Main menu where user can log in and get access to the action's menu.
    """
    while True:
        print("===== Popcorn Stats =====")
        print(" 1. Log in ")
        print("2. Menu ")
        
        option=verify_number("Select an option : ")
        if option == 1:
            client_id,__=secret_env()
            open_link(client_id)
            app.run(port=8000)
            print("Log in completed ! 🎉")
            
        if option==2:
            menu_options()
            

def menu_options():
    file=file_exist()
    if file:
        while True:
            print("1. Top 10 Popular movies !")
            print("2. Endpoint")
            print("3. Endpoint")
            choose_action=verify_number("Please, select an option :")
        
            if choose_action==1:
                see_user()
    else:
        print("You can't have access to this actions.")
        print("You must authorize your account.")
            
    

                
                
            
                
                
            
            
        
          
            