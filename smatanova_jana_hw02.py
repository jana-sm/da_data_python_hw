import json


with open('netflix_titles.tsv', mode="r", encoding='utf-8') as file:
    lines = file.readlines()


movies = []


for line in lines[1:]:
    columns = line.strip().split("\t")


    title = columns[2].strip()

    
    if columns[15] == "":
        director_items = []
    else:
        director_items = columns[15].split(",")

    directors = []
    for director in director_items:
        director = director.strip()
        if director != "":
            directors.append(director)

    
    if columns[16] == "":
        cast_items = []
    else:
        cast_items = columns[16].split(",")

    cast = []
    for actor in cast_items:
        actor = actor.strip()
        if actor != "":
            cast.append(actor)

    
    if columns[8] == "":
        genre_items = []
    else:
        genre_items = columns[8].split(",")

    genres = []
    for genre in genre_items:
        genre = genre.strip()
        if genre != "":
            genres.append(genre)

    
    year = int(columns[5].strip())
    decade = (year // 10) * 10

    movie = {
        "title": title,
        "directors": directors,
        "cast": cast,
        "genres": genres,
        "decade": decade
    }

    movies.append(movie)

with open('hw02_output.json', 'w', encoding='utf-8') as output_file:
    json.dump(movies, output_file, ensure_ascii=False, indent=4)
