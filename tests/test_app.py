from mypackage import app

def test_foo():
    s = app.foo([1,2])
    #assert s == "print foo"
    assert s == 1.5