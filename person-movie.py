from src.creation.create_node import create_node as NodeGraph
from src.creation.create_relation import create_relation as RelationGraph
from py2neo import Graph
from uuid import uuid4
from faker import Faker
from random import randint, choice
from datetime import datetime

fake = Faker()

graph = Graph("neo4j+s://030df7e1.databases.neo4j.io", auth=("neo4j", "b4VfuDIDUCu3Cbj4SpAxCjZmJtrdEkhy-nCCSMREPbg"))

def main():
    persons = []
    users = []
    movies = []
    genres = []
    
    for _ in range(5):
        user_name = fake.name()
        user_id = str(uuid4())
        labels = ["USER"]
        properties = {
            "name": user_name,
            "userId": user_id,
        }
        user_node_data = NodeGraph(graph, labels, properties)
        users.append(user_node_data)

    for _ in range(10):
        movie_title = fake.company()
        movie_id = randint(1000, 9999)
        labels = ["MOVIE"]
        properties = {
            "title": movie_title,
            "tmdbId": randint(1000, 9999),
            "released": fake.date(),
            "imdbRating": randint(0, 10),
            "movieId": movie_id,
            "year": int(fake.year()),
            'imdbId': str(uuid4()), 
            "runtime": randint(10, 420),
            "countries": fake.location_on_land()[3],
            "imdbVotes": randint(10, 9999),
            "url": fake.uri(),
            "revenue": randint(10, 99999999),
            "plot": fake.text(),
            "poster": fake.image_url(),
            "budget": randint(10, 99999999),
            "languages": fake.language_code(),
        }
        movie_node_data = NodeGraph(graph, labels, properties)
        movies.append(movie_node_data)
        
    for _ in range(7):    
        labels = ["PERSON"]
        born = fake.date_of_birth()
        properties = {
            'name': fake.name(), 
            'tmbdId':str(uuid4()), 
            'born': born, 
            'died': fake.date_between(start_date=born), 
            'bornIn': fake.location_on_land()[2], 
            'url': fake.uri(), 
            'imdbId': str(uuid4()), 
            'bio': fake.paragraph(),
            'poster': fake.image_url()
        }
        
        randi = randint(0,2)
        if randi == 0:
            labels.append("ACTOR")
        elif randi == 1:
            labels.append("DIRECTOR")
        elif randi == 2:
            labels.append("ACTOR")
            labels.append("DIRECTOR")
        
        person_node_data = NodeGraph(graph, labels, properties)
        persons.append(person_node_data)

    listGenres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western']
    for genre in listGenres:
        labels = ["GENRE"]
        properties = {
            'name': genre
        }
        genre_node_data = NodeGraph(graph, labels, properties)
        genres.append(genre_node_data)
        
    # Relation between movie and genre "IN_GENRE"
    for movie_node_data in movies:
        for _ in range(2):
            genre_node_data = choice(genres)
            RelationGraph(graph, movie_node_data["uuid"], genre_node_data["uuid"], "IN_GENRE", {})
            
    # Relation between user and Movie "RATED"
    for user_node_data in users:
        rated_movies = []
        for _ in range(2):
            movie_node_id = choice(movies)["uuid"]
            while movie_node_id in rated_movies:
                movie_node_id = choice(movies)["uuid"]

            rated_movies.append(movie_node_id)
            rating = randint(0, 5)
            properties = {
                "rating": rating,
                "timestamp": fake.unix_time(),
            }
            RelationGraph(graph, user_node_data["uuid"], movie_node_id, "RATED", properties)
            
    # Relation between PERSON DIRECTOR and Movie "DIRECTED"
    for person_node_data in persons:
        if "DIRECTOR" in person_node_data["labels"] and "ACTOR" not in person_node_data["labels"]:
            directed_movies = []
            for _ in range(2):
                movie_node_id = choice(movies)["uuid"]
                while movie_node_id in directed_movies:
                    movie_node_id = choice(movies)["uuid"]
                
                directed_movies.append(movie_node_id)
                properties = {
                    "role": "director"
                }
                RelationGraph(graph, person_node_data["uuid"], movie_node_id, "DIRECTED", properties)
            
    # Relation between PERSON ACTOR and Movie "ACTED_IN"
    for person_node_data in persons:
        if "ACTOR" in person_node_data["labels"] and "DIRECTOR" not in person_node_data["labels"]:
            acted_movies = []
            for _ in range(2):
                movie_node_id = choice(movies)["uuid"]
                while movie_node_id in acted_movies:
                    movie_node_id = choice(movies)["uuid"]
                
                acted_movies.append(movie_node_id)
                properties = {
                    "role": "actor"
                }
                RelationGraph(graph, person_node_data["uuid"], movie_node_id, "ACTED_IN", properties)
                
    # Relation between PERSON ACTOR DIRECTOR and Movie "ACTED_IN"
    for person_node_data in persons:
        if "ACTOR" in person_node_data["labels"] and "DIRECTOR" in person_node_data["labels"]:
            acted_movies = []
            directed_movies = []
            for _ in range(2):
                movie_acted_node_id = choice(movies)["uuid"]
                while movie_acted_node_id in acted_movies:
                    movie_acted_node_id = choice(movies)["uuid"]
                
                acted_movies.append(movie_acted_node_id)

                movie_directed_node_id = choice(movies)["uuid"]
                while movie_directed_node_id in directed_movies:
                    movie_directed_node_id = choice(movies)["uuid"]
                
                directed_movies.append(movie_directed_node_id)
                properties_actor = {
                    "role": "actor"
                }
                properties_director = {
                    "role": "director"
                }
                RelationGraph(graph, person_node_data["uuid"], movie_acted_node_id, "ACTED_IN", properties_actor)
                RelationGraph(graph, person_node_data["uuid"], movie_directed_node_id, "DIRECTED", properties_director)

if __name__ == "__main__":
    main()