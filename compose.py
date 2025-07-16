
def compose(f, g):
    """
    Signature: (A -> B) (C -> A) -> (C -> B)
    Purpose: Compose the given functions
    Design Idea: Return a function that applies f to the result of g
    """
    return lambda x: f(g(x))

def test_compose():
    """
    Signature: () -> None
    Purpose: Test the compose function
    Design Idea: Define some simple numeric and string functions and 
                 check the composition of the numeric functions and
                 of the string functions. Test the resulting composed
                 functions with at least 4 different inputs. Add a
                 failed string for each test: Test n failed, starting
                 with n equal to 0.
    """
    # Define some simple numeric functions
    def add1(x):
        return x + 1

    def mul2(x):
        return x * 2

    # Test the composition of numeric functions
    f = compose(mul2, add1)
    assert f(3) == 8, "Test 0 failed"
    assert f(5) == 12, "Test 1 failed"
    assert f(0) == 2, "Test 2 failed"
    assert f(-1) == 0, "Test 3 failed"

    # Define some simple string functions
    def append_exclamation(s):
        return s + "!"

    def make_uppercase(s):
        return s.upper()

    # Test the composition of string functions
    g = compose(make_uppercase, append_exclamation)
    assert g("hello") == "HELLO!", "Test 4 failed"
    assert g("world") == "WORLD!", "Test 5 failed"
    assert g("") == "!", "Test 6 failed"
    assert g("test") == "TEST!", "Test 7 failed"


test_compose()
