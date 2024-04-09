from src.creation.create_node import create_node as NodeGraph
from src.creation.create_relation import create_relation as RelationGraph
from py2neo import Graph
from uuid import uuid4
from faker import Faker
from random import randint, choice
from datetime import datetime

fake = Faker()

# graph = Graph("neo4j+s://030df7e1.databases.neo4j.io", auth=("neo4j", "b4VfuDIDUCu3Cbj4SpAxCjZmJtrdEkhy-nCCSMREPbg"))

class person:
    def __init__(self, name, tmbdId, born, died, bornIn, url, inmdbId, bio, poster):
        self.name = name


def main():
    persons = []
    users = []
    movies = []

    for _ in range(5):
        user_name = fake.name()
        user_id = str(uuid4())
        labels = ["USER"]
        properties = {
            "name": user_name,
            "userId": user_id,
        }
        # user_node_id = NodeGraph(graph, labels, properties)
        # users.append(user_node_id)
        users.append(properties)
        
    for _ in range(5):    
        labels = ["PERSON"]
        born = fake.date_of_birth()
        properties = {
            'name': fake.name(), 
            'tmbdId':str(uuid4()), 
            'born': born, 
            'died': fake.date_between(start_date=born), 
            'bornIn': fake.location_on_land()[2], 
            'url':fake.uri(), 
            'inmdbId': str(uuid4()), 
            'bio':fake.paragraph(),
            'poster':fake.image_url()
        }
        
        randi = randint(0,2)
        if randi == 0:
            labels.append("ACTOR")
        elif randi == 1:
            labels.append("DIRECTOR")
        elif randi == 2:
            labels.append("DIRECTOR")
            labels.append("ACTOR")
        # person_node_id = NodeGraph(graph, labels, properties)
        # person.append(user_node_id)
        persons.append({"labels":labels,"properties":properties})

    for _ in range(10):
        labels = ["MOVIE"]
        release_date = datetime.strptime(fake.date(),"%Y-%m-%d")
        countries = []
        for _ in range(5):
            countries.append(fake.location_on_land()[3])
        properties = {
            "title": fake.bs(),
            "tmdbId": randint(1000, 9999),
            "released": release_date,
            "imdbRating":randint(0, 10),
            "movieId":randint(1000, 9999),
            "year" : release_date,
            "runtime": randint(10, 420),
            "countries": countries,
            "imdbVotes": randint(10, 9999),
            "url":fake.uri(),
            "revenue":randint(10, 99999999),
            "plot": fake.paragraph(),
            "poster":fake.image_url(),
            "budget":randint(10, 99999999),
            "languages":countries
            
        }
        # movie_node_id = NodeGraph(graph, labels, properties)
        movies.append(properties)

    relations = []
    for user_node_id in users:
        for _ in range(2):
            movie_node_id = choice(movies)['title']
            properties = {
                "rating": randint(0, 5),
                "timestamp": fake.unix_time(),
            }
            # print(user_node_id, movie_node_id, properties)
    #         # RelationGraph(graph, user_node_id, movie_node_id, "RATED", properties)
    
    for person in persons:
        for _ in range(2):
            movie_node_id = choice(movies)['title']
            properties = {}
            if 'ACTOR' in person['labels']:
                properties["ACTED_IN"] = fake.name()
            if 'DIRECTOR' in person['labels']:
                properties["DIRECTED"] = fake.name()
            # print(person["properties"]["name"], movie_node_id, properties)
    #         # RelationGraph(graph, user_node_id, movie_node_id, "RATED", properties)
    # print(movies)
    # print(persons)
    # print(relations)

if __name__ == "__main__":
    main()