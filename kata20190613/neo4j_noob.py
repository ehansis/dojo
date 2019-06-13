import os

from neo4j import GraphDatabase


TEST_LABELS = {
    'Node': 'TestNode',
}


def get_driver():
    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", os.environ['NEO4J_PASSWORD']))
    return driver


def create_node(name):
    driver = get_driver()
    with driver.session() as session:
        return session.run("CREATE (a:%s {name:$name}) "
                           "RETURN id(a)" % TEST_LABELS['Node'],
                           name=name).single().value()


def cleanup():
    driver = get_driver()
    with driver.session() as session:
        for label in TEST_LABELS.values():
            session.run("MATCH (n:%s)"
                        "DETACH DELETE n" % label)
