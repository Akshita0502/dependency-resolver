import pytest
from app.logic import resolve_dependencies_logic


# Test 1 — valid simple dependency chain
def test_valid_simple_resolution():
    edges = [["B", "A"], ["C", "B"]]  # A → B → C
    result = resolve_dependencies_logic(edges)
    assert "order" in result
    assert result["order"].index("A") < result["order"].index("B")
    assert result["order"].index("B") < result["order"].index("C")


# Test 2 — cycle detection (A depends on B, B depends on A)
def test_cycle_detection():
    edges = [["A", "B"], ["B", "A"]]
    result = resolve_dependencies_logic(edges)
    assert "cycle" in result
    assert len(result["cycle"]) > 0


# Test 3 — empty input (no dependencies)
def test_empty_edges():
    edges = []
    result = resolve_dependencies_logic(edges)
    assert "order" in result
    assert result["order"] == []


# Test 4 — single node, no dependencies
def test_single_node():
    edges = [["B", "A"]]
    result = resolve_dependencies_logic(edges)
    assert "order" in result
    assert "A" in result["order"]
    assert "B" in result["order"]


#Test 5 — longer cycle (3 nodes)
def test_three_node_cycle():
    edges = [["B", "A"], ["C", "B"], ["A", "C"]]
    result = resolve_dependencies_logic(edges)
    assert "cycle" in result


#Test 6 — multiple independent chains
def test_multiple_independent_chains():
    edges = [["B", "A"], ["D", "C"]]  # A→B and C→D independent
    result = resolve_dependencies_logic(edges)
    assert "order" in result
    assert "A" in result["order"]
    assert "C" in result["order"]


#Test 7 — no cycle returns no cycle key
def test_valid_graph_has_no_cycle_key():
    edges = [["B", "A"], ["C", "B"]]
    result = resolve_dependencies_logic(edges)
    assert "cycle" not in result