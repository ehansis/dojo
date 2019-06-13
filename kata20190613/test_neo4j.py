from . import neo4j_noob


def test_get_driver():
    neo4j_noob.get_driver()


def test_create_node():
    i = neo4j_noob.create_node('FooBar')
    assert i >= 0
    neo4j_noob.cleanup()
