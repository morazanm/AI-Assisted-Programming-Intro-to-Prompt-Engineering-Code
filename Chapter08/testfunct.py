def test_funct(funct, inputs, outputs):
    """
    Signature: (X -> Y) (listof X) (listof Y) -> None
    Purpose: Tests function f with given inputs and expected outputs.
    Design Idea: Iterate through inputs and outputs to check if for corresponding elements, i and o, f(i)=o.
    """
    testvals = inputs
    results = outputs
    for testval, result in zip(testvals, results):
        msg = f"Test failed for input {testval}: expected {result}, got {funct(testval)}"
        assert funct(testval) == result, msg