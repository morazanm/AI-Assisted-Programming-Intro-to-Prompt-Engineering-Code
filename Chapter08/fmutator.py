import testfunct

x = 20

def f(y):
    """
    Signature: number -> number
    Purpose: Increment x by 10 and return its value
    Design Idea: Mutate x by adding y to it
    """
    global x 
    x = x + y
    return x

#def test_f():
#    testfunct.test_funct(f, [0, 1, 2, 3], [20, 21, 23, 26])

def test_f():
    """
    Signature: () -> None
    Purpose: Tests the f function
    Design Idea: Test using different values for y.
    """
    assert f(0) == 20, "Test failed for input 0"
    assert f(1) == 21, "Test failed for input 1"
    assert f(2) == 23, "Test failed for input 2"
    assert f(3) == 26, "Test failed for input 3"

test_f()


