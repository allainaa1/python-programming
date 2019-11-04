marvel_movies = ["Iron Man", "Captain America: Civil War", "Black Panther", "Ant-Man and the Wasp", "Captain Marvel", "Guardians of the Galaxy", "Doctor Strange", "Ant-Man", "The Incredible Hulk", "Thor"]
special_marvel_movies = []
for movie in marvel_movies:
    if "the" in movie:
        print(marvel_movies[movie])