import json
import logging
from openai import OpenAI


class OpenAIGenerator:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.client = OpenAI()

    def get_knowledge_graph(self, input_text):
        preprompt = """Given the provided input text below, your task is to construct a knowledge graph by discerning relationships within the text. The objective is to extract significant entities representing nodes in the graph. Each node should possess an ID, a label (the word itself), and its Named Entity Recognition (NER) tag. Furthermore, establish directed edges between nodes to signify relationships, with each edge containing the IDs of the nodes it connects and a label describing the relationship. Ensure that the relationship label is significant, such as action or preposition. The final output should be a JSON representation of the graph. Do not include any extraneous information.
        Example:
        Input text: "Toto is Tata's friend"
        Response:
        {
            "nodes": {
            "1": {"label": "Toto", "ner_tag": "B-PERSON"},
            "2": {"label": "is", "ner_tag": "O"},
            "3": {"label": "Tata", "ner_tag": "B-PERSON"},
            "4": {"label": "friend", "ner_tag": "O"}
            },
            "edges": [{"from": "1", "to": "3", "label": "friend"}]
        }
        
        Input text: 
        """

        return self.get_json_response(preprompt, input_text)

    def get_ner(self, input_text):
        preprompt = """Given a text, generate a Named Entity Recognition (NER) tagging dataset in the Beginning, Inside, Outside (BIO) format. The dataset should consist of a list of tokens and a list of labels, both in Python list format. For example, tokens=['word1','word2','word3'], labels=['O','B-PERSON','I-PERSON']. The goal is to identify and tag entities within the text, such as people, organizations, and locations.
        Here is the input text: 
        """
        return self.get_json_response(preprompt, input_text)

    def get_json_response(
        self,
        preprompt,
        input_text,
    ):

        messages = [
            {"role": "user", "content": preprompt + input_text},
        ]

        response = self.client.chat.completions.create(
            model=self.model, messages=messages, temperature=0
        )

        try:
            extract_json = json.loads(response.choices[0].message.content)
        except Exception as e:
            print("Not valid text", response.choices[0].message.content)
            logging.error(
                e,
                f"Response from document is not jsonifiable",
            )

            return None
        return extract_json
