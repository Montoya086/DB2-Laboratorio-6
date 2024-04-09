from src.creation.create_node import create_node as NodeGraph
from src.creation.create_relation import create_relation as RelationGraph
from src.query.user_movie_query import user_movie_query as UserMovieQuery
from py2neo import Graph
from uuid import uuid4
from faker import Faker
from random import randint, choice

fake = Faker()

graph = Graph("neo4j+s://030df7e1.databases.neo4j.io", auth=("neo4j", "b4VfuDIDUCu3Cbj4SpAxCjZmJtrdEkhy-nCCSMREPbg"))

def main():
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
        user_node_data = NodeGraph(graph, labels, properties)
        users.append(user_node_data["uuid"])

    for _ in range(10):
        movie_title = fake.company()
        movie_id = randint(1000, 9999)
        labels = ["MOVIE"]
        properties = {
            "title": movie_title,
            "movieId": movie_id,
            "year": int(fake.year()),
            "plot": fake.text(),
        }
        movie_node_data = NodeGraph(graph, labels, properties)
        movies.append(movie_node_data["uuid"])

    for user_node_id in users:
        rated_movies = []
        for _ in range(2):
            movie_node_id = choice(movies)
            while movie_node_id in rated_movies:
                movie_node_id = choice(movies)

            rated_movies.append(movie_node_id)
            rating = randint(0, 5)
            properties = {
                "rating": rating,
                "timestamp": fake.unix_time(),
            }
            RelationGraph(graph, user_node_id, movie_node_id, "RATED", properties)


if __name__ == "__main__":
    main()