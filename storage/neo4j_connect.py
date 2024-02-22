import os
from neo4j import GraphDatabase


class Neo4jConnection:

    def __init__(self):
        uri = f"bolt://{os.environ('NEO4J_HOST')}:{os.environ('NEO4J_PORT')}"
        self.driver = GraphDatabase.driver(
            uri, auth=(os.environ("NEO4J_LOGIN"), os.environ("NEO4J_PASSWORD"))
        )

    def close(self):
        self.driver.close()

    def create_and_return_triplet(self, tail, head, rel):
        """
        Create a triplet in the graph and return the text of the tail and head nodes

        """
        with self.driver.session() as session:
            result = session.run(
                """
                            CALL apoc.merge.node([$tail_type],{text:$tail_text} )
                            YIELD node as a
                            CALL apoc.merge.node([$head_type],{text:$head_text} )
                            YIELD node as b
                            WITH a,b
                            CALL apoc.merge.relationship(a, toUpper(replace($rel,' ', '_')), {}, {}, b, {})
                            YIELD rel
                            RETURN a.text + '  ' + b.text
                            """,
                tail_type=tail["type"],
                tail_text=tail["text"],
                head_type=head["type"],
                head_text=head["text"],
                rel=rel,
            )
            return result.single()[0]
