from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_graph_traversal_endpoint_contract():
    response = client.get(
        "/knowledge/graph/traversal/doc-1"
    )

    assert response.status_code == 200

    body = response.json()

    assert "nodes" in body
    assert "depth" in body
    assert isinstance(body["nodes"], list)



def test_graph_traversal_depth_parameter():
    response = client.get(
        "/knowledge/graph/traversal/doc-1?depth=2"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["depth"] == 2



def test_graph_traversal_response_schema():
    response = client.get(
        "/knowledge/graph/traversal/doc-1"
    )

    assert response.status_code == 200

    nodes = response.json()["nodes"]

    for node in nodes:
        assert "id" in node
        assert "node_type" in node
        assert "metadata" in node



def test_graph_traversal_invalid_zero_depth():
    response = client.get(
        "/knowledge/graph/traversal/doc-1?depth=0"
    )

    assert response.status_code == 422



def test_graph_traversal_invalid_negative_depth():
    response = client.get(
        "/knowledge/graph/traversal/doc-1?depth=-1"
    )

    assert response.status_code == 422
