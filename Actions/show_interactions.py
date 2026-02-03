from Actions.interactions import top_movies

def show_topmovie(movies_json):
    movies_json=top_movies()
    for movie in movies_json:
         title=movie["title"]
         trailer=movie["trailer"]
         print(title,trailer)
    return
