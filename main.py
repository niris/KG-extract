import os

from dotenv import load_dotenv
from reader.csv_to_graph import extract_csv_to_graphs
from storage.storageManager import populate_neo4j_from_list


def main():
    graphs = extract_csv_to_graphs(
        os.path.join("files", "input", "test.csv"), save_to_json=True
    )
    populate_neo4j_from_list(graphs)


if __name__ == "__main__":
    load_dotenv()

    main()
