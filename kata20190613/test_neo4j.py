from . import neo4j_noob


def test_get_driver():
    neo4j_noob.get_driver()


def test_create_node():
    neo4j_noob.cleanup()
    i = neo4j_noob.create_node('FooBar')
    assert i >= 0


def test_create_relationship():
    neo4j_noob.cleanup()
    neo4j_noob.create_node('Node1')
    neo4j_noob.create_node('Node2')
    assert neo4j_noob.query_node_count() == 2

    res = neo4j_noob.create_relationship('likes', 'Node1', 'Node2')
    assert res.single().value() >= 0

    count = neo4j_noob.query_relationship_count()
    assert count == 1

    rel = neo4j_noob.query_relationships().records()
    count_2 = 0
    for _ in rel:
        count_2 += 1
    assert count_2 == 1


def test_create_relationship_node_missing():
    neo4j_noob.cleanup()
    neo4j_noob.create_node('Node1')
    res = neo4j_noob.create_relationship('likes', 'Node1', 'Node2')
    assert res.single() is None
    assert neo4j_noob.query_relationship_count() == 0


def test_create_relationship_with_merge():
    neo4j_noob.cleanup()
    neo4j_noob.create_relationship_with_merge('likes', 'Node1', 'Node2')
    assert neo4j_noob.query_relationship_count() == 1
    assert neo4j_noob.query_node_count() == 2

    neo4j_noob.create_relationship_with_merge('hates', 'Node2', 'Node3')
    assert neo4j_noob.query_relationship_count() == 2
    assert neo4j_noob.query_node_count() == 3

    neo4j_noob.create_relationship_with_merge('loves', 'Node2', 'Node1')
    assert neo4j_noob.query_relationship_count() == 3
    assert neo4j_noob.query_node_count() == 3
