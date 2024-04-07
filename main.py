from src.creation.create_node import create_node as NodeGraph
from src.creation.create_relation import create_relation as RelationGraph
from py2neo import Graph

graph = Graph("neo4j+s://030df7e1.databases.neo4j.io", auth=("neo4j", "b4VfuDIDUCu3Cbj4SpAxCjZmJtrdEkhy-nCCSMREPbg"))

def main():
    labels = ["Person", "Customer"]
    properties = {
        "name": "John Doe",
        "email": "john@doe.com",
    }

    n1=NodeGraph(graph, labels, properties)

    labels = ["Person", "Customer"]
    properties = {
        "name": "Jane Doe",
        "email": "jane@doe.com",
    }
    n2 = NodeGraph(graph, labels, properties)

    relation = "KNOWS"
    properties = {
        "since": "2020-01-01",
    }
    r1 = RelationGraph(graph, n1, n2, relation, properties)

    print(f"Relation UUID: {r1}")


if __name__ == "__main__":
    main()