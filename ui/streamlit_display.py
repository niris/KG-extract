import streamlit as st
import graphviz

from extractor.graph_tranformer import (
    extract_graphs_edges,
    extract_graph_edges,
)
from extractor.openai_generator import OpenAIGenerator


def display_main_interface():
    st.header("KG-Extract", divider="red")
    tab1, tab2 = st.tabs(["Text to Graph", "CSV to Graph"])
    with tab1:
        text_input = st.text_area("Enter the text to extract the graph from")
        if text_input:
            openai_client = OpenAIGenerator()
            knowledge_graph_elements = openai_client.get_knowledge_graph(text_input)
            edges = extract_graph_edges(knowledge_graph_elements)
            display_graph(edges)

    with tab2:
        csv_file = st.file_uploader("Upload a CSV file")
        # TODO: Implement the CSV to graph extraction


def display_graph(graph_eges):
    """
    Display a graph given as a list of edges
    """
    graph = graphviz.Digraph()
    for edge in graph_eges:
        graph.edge(edge[0]["text"], edge[1]["text"], label=edge[2])

    st.graphviz_chart(graph)


def display_graphs(graphs):
    """
    Display a list of graphs given as a list of dictionaries
    Args:
    graphs: list of graphs elements in the form of a list of dictionaries with the following keys
            - "nodes": list of nodes, each node is a dictionary with keys "id","label" and "ner_tag"
            - "edges": list of edges, each edge is a dictionary with keys "from","to" and "label". From and to are the ids of the nodes
    """
    edges = extract_graphs_edges(graphs)
    graph = graphviz.Digraph()
    for edge in edges:
        graph.edge(edge[0]["text"], edge[1]["text"])

    st.graphviz_chart(graph)
