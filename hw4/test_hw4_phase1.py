from typing import Optional
from weightedgraph import *
from dijkstra import dijkstra

def test_task1_city_1() -> None:
    g = WeightedGraph("cities", "roads")
    assert "South Fulton" in g.vertices
    assert g.vertices["South Fulton"].name == "South Fulton"
    assert g.vertices["South Fulton"].x == 874
    assert g.vertices["South Fulton"].y == 363

def grading_get_hsf() -> Optional[Edge]:
    g = WeightedGraph("cities", "roads")
    h = g.vertices.get("Hendersonville")
    assert h
    hsf = None
    for e in h.edges:
        if (e.a.name == "Hendersonville" and e.b.name == "South Fulton") or \
           (e.a.name == "South Fulton" and e.b.name == "Hendersonville"):
            hsf = e
            break
    return hsf

def test_task1_road_1() -> None:
    hsf = grading_get_hsf()
    assert hsf
    assert hsf.speed == 45
    assert hsf.toll == 125
    assert hsf.ugly == 10

def grading_close(x: float, y: float) -> bool:
     return abs(x - y) < 0.001

def test_task1_weight_1() -> None:
    hsf = grading_get_hsf()
    assert hsf
    assert grading_close(hsf.weight(Metric.Distance), 75)
    assert grading_close(hsf.weight(Metric.Time), 1.66666667)

def test_task3_distance_1() -> None:
    g = WeightedGraph("cities", "roads")
    ic = g.vertices.get("Inglewood City")
    hg = g.vertices.get("Hartford Gardens")
    assert ic
    assert hg
    p = dijkstra(g, ic, hg, Metric.Distance)
    assert len(p) == 3
    assert {p[0].a.name, p[0].b.name} == {"Inglewood City", "Los Lunas"}
    assert {p[1].a.name, p[1].b.name} == {"Los Lunas", "Lansing"}
    assert {p[2].a.name, p[2].b.name} == {"Lansing", "Hartford Gardens"}
