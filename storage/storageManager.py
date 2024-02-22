import csv
from storage.neo4j_connect import Neo4jConnection


def populate_neo4j_from_list(graph_list):
    """
    Connect to the Neo4j database and insert the graphs from the list of graph data
    the graph data should be a list of dictionaries with the following keys
    - "nodes": list of nodes, each node is a dictionary with keys "id","label" and "ner_tag"
    - "edges": list of edges, each edge is a dictionary with keys "from","to" and "label". From and to are the ids of the nodes
        Example:
        graph_list = [
                "nodes": {
                    1:{"label": "Toto", "ner_tag": "B-PERSON"},
                    2:{"label": "is", "ner_tag": "O"},
                    3:{"label": "Tata", "ner_tag": "B-PERSON"},
                    4:{"label": "friend", "ner_tag": "O"}
                ,
                "edges": [{"from": 1, "to": 3, "label": "friend"}]
                }

        ]
    """

    neo4j_connection = Neo4jConnection()

    for graph in graph_list:
        nodes = graph["nodes"]

        for edge in graph["edges"]:
            tail = {
                "type": nodes[edge["from"]]["ner_tag"],
                "text": nodes[edge["from"]]["label"],
            }
            head = {
                "type": nodes[edge["to"]]["ner_tag"],
                "text": nodes[edge["to"]]["label"],
            }
            neo4j_connection.create_and_return_triplet(tail, head, edge["label"])
    neo4j_connection.close()


def populate_neo4j_from_csv(csv_path):
    """
    Connect to the Neo4j database and insert the graphs from the csv file
    The csv file should have columns respecting the following order:
    tail_text, tail_type, head_text, head_type, relationship
    """
    neo4j_connection = Neo4jConnection()
    with open(csv_path, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            tail = {"type": row[1], "text": row[0]}
            head = {"type": row[3], "text": row[2]}
            neo4j_connection.create_and_return_triplet(tail, head, row[4])
    neo4j_connection.close()
