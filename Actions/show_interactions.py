from Actions.interactions import top_movies

def show_topmovie(movies_json):
    print("--- Top movies --- ")
    for i,movie in enumerate(movies_json,start=1):
         title=movie["title"]
         trailer=movie["trailer"]
         print(f"- {i} {title}, {trailer}")
    return
