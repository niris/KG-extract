from neo4j import GraphDatabase

class GraphConnect:
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    """
    def print_info(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_triplet, message)
            print(greeting)
    """

    def create_and_return_triplet(self,tail,head,rel):
        with self.driver.session() as session:
            result = session.run("""
                            CALL apoc.merge.node([$tail_type],{text:$tail_text} )
                            YIELD node as a
                            CALL apoc.merge.node([$head_type],{text:$head_text} )
                            YIELD node as b
                            WITH a,b
                            CALL apoc.merge.relationship(a, toUpper(replace($rel,' ', '_')), {}, {}, b, {})
                            YIELD rel
                            RETURN a.text + '  ' + b.text
                            """, tail_type=tail['type'],tail_text=tail['text'],head_type=head['type'],head_text=head['text'],rel=rel)
            return result.single()[0]


if __name__ == "__main__":
    greeter = GraphConnect("bolt://localhost:7687", "neo4j", "mypassword")
    tail = {"type":"Person","text":"Jame"}
    head = {"type":"Place","text":"Osaka"}
    res= greeter.create_and_return_triplet(tail,head,"Like")
    print(res)
    greeter.close()