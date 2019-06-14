import os

from neo4j import GraphDatabase


TEST_LABELS = ['TestNode']


_driver = None


def get_driver():
    global _driver

    if _driver is None:
        uri = "bolt://localhost:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", os.environ['NEO4J_PASSWORD']))
        _driver = driver

    return _driver


def create_node(name):
    driver = get_driver()
    with driver.session() as session:
        return session.run("CREATE (a:TestNode {name:$name}) "
                           "RETURN id(a)",
                           name=name).single().value()


def create_relationship(label, name_from, name_to):
    driver = get_driver()
    with driver.session() as session:
        # using parameters for relationship types is not supported, see
        # https://neo4j.com/docs/cypher-manual/current/syntax/parameters/
        return session.run("MATCH (from:TestNode {name:$name_from}),"
                           "      (to:TestNode {name:$name_to})"
                           "CREATE (from)-[rel:%(label)s]->(to)"
                           "RETURN id(rel)" % {'label': label},
                           name_from=name_from, name_to=name_to)


def query_relationship_count():
    driver = get_driver()
    with driver.session() as session:
        res = session.run("MATCH ()-[rel]->()"
                          "RETURN COUNT(rel)").single()
        if res is None:
            return 0
        else:
            return res.value()


def query_node_count():
    driver = get_driver()
    with driver.session() as session:
        res = session.run("MATCH (n)"
                          "RETURN COUNT(n)").single()
        if res is None:
            return 0
        else:
            return res.value()


def query_relationships():
    driver = get_driver()
    with driver.session() as session:
        return session.run("MATCH ()-[rel]->()"
                           "RETURN rel")


def create_relationship_with_merge(label, name_from, name_to):
    driver = get_driver()
    with driver.session() as session:
        # using parameters for relationship types is not supported, see
        # https://neo4j.com/docs/cypher-manual/current/syntax/parameters/
        return session.run("MERGE (from:TestNode {name:$name_from})"
                           "MERGE (to:TestNode {name:$name_to})"
                           "MERGE (from)-[rel:%(label)s]->(to)"
                           "RETURN ID(rel)" % {'label': label},
                           name_from=name_from, name_to=name_to)


def cleanup():
    driver = get_driver()
    with driver.session() as session:
        for label in TEST_LABELS:
            session.run("MATCH (n:%s)"
                        "DETACH DELETE n" % label)
