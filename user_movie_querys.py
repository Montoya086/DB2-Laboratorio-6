from src.query.user_movie_query import user_movie_query as UserMovieQuery, user_query as UserQuery, movie_query as MovieQuery
from py2neo import Graph

graph = Graph("neo4j+s://030df7e1.databases.neo4j.io", auth=("neo4j", "b4VfuDIDUCu3Cbj4SpAxCjZmJtrdEkhy-nCCSMREPbg"))

def main():
    print("\nUser Query")
    print(UserQuery(graph, "13fb6cab-c073-46c6-9966-d0934e6bc37f"))
    print("\nMovie Query")
    print(MovieQuery(graph, "9b60dbfe-fe53-4461-890f-23841a3a742a"))
    print("\nUser Movie Query")
    print(UserMovieQuery(graph, "13fb6cab-c073-46c6-9966-d0934e6bc37f", "9b60dbfe-fe53-4461-890f-23841a3a742a"))

if __name__ == "__main__":    
    main()





