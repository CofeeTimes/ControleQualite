from mycode import my_fct

def test_my_fct():
    assert my_fct(0) == 0 # Result 0 if not problem

def test_my_fct_not_0():
    assert my_fct(1) == 11