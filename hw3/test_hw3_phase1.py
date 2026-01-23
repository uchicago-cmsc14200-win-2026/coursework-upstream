from graph import *
from wordgraphs import *

def test_task1_is_word_1() -> None:
    g = PrecompGraph("web2", 4)
    assert g.is_actual_word("code")

def test_task1_is_not_word_1() -> None:
    g = PrecompGraph("web2", 4)
    assert not g.is_actual_word("abcd")

def test_task1_adjacent_1() -> None:
    g = PrecompGraph("web2", 4)
    actual = g.adjacent("code")
    expected = {'bode', 'cade', 'cede', 'coda', 'codo', 'coke', 'cole', 'come',
                'cone', 'cope', 'core', 'cote', 'coue', 'cove', 'coze', 'dode',
                'gode', 'lode', 'mode', 'node', 'rode', 'tode', 'wode'}
    assert actual == expected

def test_task1_degree_1() -> None:
    g = PrecompGraph("web2", 4)
    assert g.degree("code") == 23

def test_task2c_1() -> None:
    g = PrecompGraph("web2", 6)
    actual = variations(g, "lanius", 3, False)
    
    assert len(actual) == 0

def test_task3_1() -> None:
    g = PrecompGraph("web2", 4)
    actual = shortest_word_path(g, "long", "path")
    allowable = [['long', 'lone', 'lote', 'pote', 'pate', 'path'],
                 ['long', 'lone', 'lote', 'late', 'lath', 'path'],
                 ['long', 'lone', 'lote', 'late', 'pate', 'path'],
                 ['long', 'lone', 'lane', 'pane', 'pate', 'path'],
                 ['long', 'lone', 'lane', 'late', 'lath', 'path'],
                 ['long', 'lone', 'lane', 'late', 'pate', 'path'],
                 ['long', 'lone', 'pone', 'pote', 'pate', 'path'],
                 ['long', 'lone', 'pone', 'pane', 'pate', 'path'],
                 ['long', 'pong', 'pone', 'pote', 'pate', 'path'],
                 ['long', 'pong', 'pone', 'pane', 'pate', 'path'],
                 ['long', 'pong', 'pang', 'pane', 'pate', 'path'],
                 ['long', 'tong', 'tang', 'tanh', 'tath', 'path']]
                
    assert actual in allowable

def test_task4c_is_word_1() -> None:
    g = LazyGraph("web2")
    assert g.is_actual_word("parsimonious")

def test_task4c_is_not_word_1() -> None:
    g = LazyGraph("web2")
    assert not g.is_actual_word("abcd")

def test_task4c_adjacent_1() -> None:
    g = LazyGraph("web2")
    actual = g.adjacent("code")
    expected = {'bode', 'cade', 'cede', 'coda', 'codo', 'coke', 'cole', 'come',
                'cone', 'cope', 'core', 'cote', 'coue', 'cove', 'coze', 'dode',
                'gode', 'lode', 'mode', 'node', 'rode', 'tode', 'wode'}
    assert actual == expected

def test_task4c_degree_1() -> None:
    g = LazyGraph("web2")
    assert g.degree("code") == 23
