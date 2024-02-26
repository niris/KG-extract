import os
import csv
import json

from extractor.openai_generator import OpenAIGenerator


def extract_csv_to_graph_elements(file_path, save_to_json=False):
    """
    Extracts a list of nodes and edges between them from a CSV file.
    If save_to_json is True, it saves each graph as a JSON file in the output directory.
    """

    graphs_elements = []
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    openai_client = OpenAIGenerator()

    with open(file_path, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the first line
        for line_num, row in enumerate(csvreader, start=1):
            graph = openai_client.get_knowledge_graph(row[1])

            if graph:
                graphs_elements.append(graph)
                # Save graph to a JSON file
                if save_to_json:
                    output_path = os.path.join("files", "output", "json", file_name)
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)

                    graph_info = {str(line_num): {"text": row[1], "graph": graph}}
                    with open(
                        os.path.join(output_path, str(line_num) + ".json"), "w"
                    ) as json_file:
                        json.dump(graph_info, json_file, indent=4)
    return graphs_elements
