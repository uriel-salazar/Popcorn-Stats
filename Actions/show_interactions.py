
def show_movie(movies_json):
     """ Iterates popular movies and shows them to the user.

     Args:
         movies_json (dict): 10 Popular movies dict
     """
     print("--- Top movies --- ")
     for i,movie in enumerate(movies_json,start=1):
         title=movie["title"]
         trailer=movie["trailer"]
         print(f"- {i} {title}, {trailer}")

def display_show(shows_json):
     """ Iterates popular shows and shows them to the user.
     It shows the title of the show, the trailer and the rating.

     Args:
         shows_json (dict): 10 Popular shows dict
     """
     print("--- Top Shows ---")
     for i,show in enumerate(shows_json,start=1):
          title=show["title"]
          trailer=show["trailer"]
          rating=show["rating"]
          print(f"- {i} {title}, {trailer} rating :{rating:.2f}")


def show_search_movies(found_movie):
     """ Shows the movies found by the user's search

     Args:
         found_movie (dict): Movies found.
     """
     print("--- Results from your search --- ")
     for i,movie in enumerate(found_movie,start=1):
          title=movie["movie"]["title"]
          print(f"- {i} {title}")
