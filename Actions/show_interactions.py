from Actions.interactions import top_movies

def show_movie(movies_json):
    print("--- Top movies --- ")
    for i,movie in enumerate(movies_json,start=1):
         title=movie["title"]
         trailer=movie["trailer"]
         print(f"- {i} {title}, {trailer}")
    return

def display_show(shows_json):
     print("--- Top Shows ---")
     for i,show in enumerate(shows_json):
          title=show["title"]
          trailer=show["trailer"]
          rating=show["rating"]
          print(f"- {i} {title}, {trailer} rating :{rating:.2f}")


def show_search_movies(found_movie):
     print("--- Results from your search ")
     for i,movie in enumerate(found_movie):
         pass