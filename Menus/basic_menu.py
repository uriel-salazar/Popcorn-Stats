from OAuth.api_config import file_exist
from Actions.show_interactions import show_topmovie,show_topshow
from Actions.interactions import top_movies,top_show
from Validate.validate_input import verify_number
from OAuth.authorization_class import UserAuth,app

def menu():
    """ Main menu where user can log in and get access to the action's menu.
    """
    while True:
        print("===== Popcorn Stats =====")
        print(" 1. Log in ")
        print("2. Menu ")
        
        option=verify_number("Select an option : ")
        if option == 1:
            user=UserAuth()
            user.secret_env()
            user.open_link()
            app.run(port=8000)

        elif option==2:
            menu_options()
            

def menu_options():
    file=file_exist()
    if file:
        while True:
            print("1. Top 10 Popular movies !")
            print("2. Top 10 Popular shows ! ")
            print("3. Endpoint")
            choose_action=verify_number("Please, select an option :")
        
            if choose_action==1:
                movies_json=top_movies()
                show_topmovie(movies_json)
                return
                
            elif choose_action==2:
                 shows_json=top_show()
                 show_topshow(shows_json)
       
    else:
        print("Please, authorize your account first.")
            
    

                
                
            
                
                
            
            
        
          
            