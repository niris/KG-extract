import os
from dotenv import load_dotenv

from reader.csv_to_graph import extract_csv_to_graph_elements
from storage.storageManager import populate_neo4j_from_list
from ui.streamlit_display import display_main_interface


def display_interface():
    """
    Main function for running graph extraction interface
    """
    display_main_interface()


def run_csv_to_graph_and_neo4j_storage():
    """
    Run the extraction of graphs from a csv file and store them in the Neo4j database
    """
    graphs = extract_csv_to_graph_elements(
        os.path.join("files", "input", "test.csv"), save_to_json=True
    )
    populate_neo4j_from_list(graphs)


if __name__ == "__main__":
    load_dotenv()

    # extract graph and choose to store them on neo4j via the interface
    display_interface()

    # extract the graphs from a csv file and store them in the Neo4j database without displaying the interface
    # run_csv_to_graph_and_neo4j_storage()
