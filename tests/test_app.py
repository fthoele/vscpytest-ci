from pytest import fixture

from mypackage import app

@fixture
def datadir(request):
    import os
    filename = request.module.__file__
    test_dir = os.path.dirname(filename)

    def getter(filename):
        return os.path.join(test_dir, "data", filename)

    return getter

def test_foo():
    s = app.foo([1,2])
    #assert s == "print foo"
    assert s == 1.5


def test_foo_from_file(datadir):
    filename = datadir("test.txt")
    #assert filename == "test.txt"
    
    x = app.foo_from_file(filename)
    assert x == 2.0