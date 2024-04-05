def create_node(tx, labels, properties):
    # Unir todas las etiquetas en una cadena separada por dos puntos.
    label_str = ":".join(labels)
    query = f"CREATE (n:{label_str} $properties)"
    tx.run(query, properties=properties)