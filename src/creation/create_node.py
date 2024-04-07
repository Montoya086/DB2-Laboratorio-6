from py2neo import Graph
from uuid import uuid4

def create_node(graph: Graph, labels: list[str], properties = {})-> str:
    # Unir todas las etiquetas en una cadena separada por dos puntos.
    label_str = ":".join(labels)
    properties["uuid"] = str(uuid4())
    query = f"MERGE (n:{label_str} $properties)"
    graph.run(query, properties=properties)
    return properties["uuid"]