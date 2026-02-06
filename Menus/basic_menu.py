from OAuth.api_config import file_exist
from Actions.show_interactions import show_movie,display_show,show_search_movies
from Actions.interactions import top_movies,top_show,search_movie
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
            print("3. Search movie")
            choose_action=verify_number("Please, select an option :")
        
            if choose_action==1:
                movies_json=top_movies()
                if movies_json==None:
                     print("Please, check your internet and try again.")
                else:
                    show_movie(movies_json)
                return
                
            elif choose_action==2:
                 shows_json=top_show()
                 if shows_json==None:
                     print("Please, check your internet and try again.")
                 else:
                     display_show(shows_json)
                 
            elif choose_action==3:
                 found_movie=search_movie()
                 if found_movie==None:
                    print("Please, check your internet and try again.")
                 else:
                     show_search_movies(found_movie)
                     
                
       
    else:
        print("Please, authorize your account first.")
            
    

                
                
            
                
                
            
            
        
          
            