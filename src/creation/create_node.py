from py2neo import Graph
from uuid import uuid4

def create_node(graph: Graph, labels: list[str], properties = {})-> dict[
    str,
    list[str]
]:
    # Unir todas las etiquetas en una cadena separada por dos puntos.
    label_str = ":".join(labels)
    print(label_str)
    properties["uuid"] = str(uuid4())
    query = f"CREATE (n:{label_str} $properties)"
    graph.run(query, properties=properties)
    return {
        "uuid": properties["uuid"],
        "labels": labels
    }