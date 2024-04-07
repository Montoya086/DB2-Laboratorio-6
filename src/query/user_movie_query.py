from py2neo import Graph

def user_movie_query(graph: Graph, user1UUID: str, movie1UUID: str):
    query = f"MATCH (a:USER {{uuid: '{user1UUID}'}})-[r:RATED]->(b:MOVIE {{uuid: '{movie1UUID}'}}) RETURN a, r, b"
    return graph.run(query).data()