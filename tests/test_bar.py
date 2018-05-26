from mypackage.submodule import mod

def test_bar():
    s = mod.bar()
    assert s == "function bar"