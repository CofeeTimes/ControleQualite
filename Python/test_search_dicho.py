from search_dicho import search

def test_search():
    assert search([1, 2, 3, 4, 5], 5, 3) == 2

def test_search_not_inside_1():
    assert search([1, 2, 3, 4, 5], 5, 6) == -1

def test_search_not_inside_2():
    assert search([1, 2, 3, 4, 5], 5, 0) == -1