from py2neo import Graph
from uuid import uuid4

def create_relation(graph: Graph, node1UUID: str, node2UUID: str, relation: str, properties = {}) -> str:
    properties["uuid"] = str(uuid4())
    query = f"MATCH (a) WHERE a.uuid = '{node1UUID}' MATCH (b) WHERE b.uuid = '{node2UUID}' MERGE (a)-[r:{relation} $properties]->(b)"
    graph.run(query, properties=properties)
    return properties["uuid"]
