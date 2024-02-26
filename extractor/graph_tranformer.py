def extract_graph_nodes(graph):
    """
    Extracts the nodes from a graph element (nodes and edges).
    """
    return graph["nodes"]


def extract_graphs_nodes(graphs):
    """
    Extracts the nodes from a list of graphs elements (nodes and edges).
    Args:
        graphs: list of graphs elements in the form of a list of dictionaries with the following keys
        - "nodes": list of nodes, each node is a dictionary with keys "id","label" and "ner_tag"
        - "edges": list of edges, each edge is a dictionary with keys "from","to" and "label". From and to are the ids of the nodes
    """
    graphs_nodes = []
    for graph in graphs:
        graphs_nodes.extend(extract_graph_nodes(graph))
    return graphs_nodes


def extract_graph_edges(graph):
    """
    Extracts the edges from a graph element (nodes and edges).
    """
    print(graph)
    if not graph:
        return []

    edges = []
    nodes = graph["nodes"]

    for edge in graph["edges"]:
        tail_node = nodes[edge["from"]]
        head_node = nodes[edge["to"]]

        tail = {"type": tail_node["ner_tag"], "text": tail_node["label"]}
        head = {"type": head_node["ner_tag"], "text": head_node["label"]}

        edges.append((tail, head, edge["label"]))

    return edges


def extract_graphs_edges(graphs):
    """
    Extracts the edges from a list of graphs elements (nodes and edges).
    Args:
        graphs: list of graphs elements in the form of a list of dictionaries with the following keys
        - "nodes": list of nodes, each node is a dictionary with keys "id","label" and "ner_tag"
        - "edges": list of edges, each edge is a dictionary with keys "from","to" and "label". From and to are the ids of the nodes
    """
    graphs_edges = []

    for graph in graphs:
        graphs_edges.extend(extract_graph_edges(graph))

    return graphs_edges
