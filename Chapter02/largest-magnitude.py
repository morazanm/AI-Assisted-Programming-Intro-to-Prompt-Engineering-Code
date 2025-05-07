def largest_magnitude(x, y):
    # Signature: number number -> number
    # Purpose: Returns the number with the largest magnitude
    #: Design idea: Compare the absolute values of the two numbers
    #               and return the one with the largest absolute value
    if abs(x) >= abs(y):
        return x
    else:
        return y

def test_largest_magnitude():
    # Test several numbers with equal magnitudes
    # Test several numbers with different magnitudes
    # Test positive and negative numbers
    assert largest_magnitude(1, 2) == 2, \
           "largest_magnitude: test case 0 failed" 
    assert largest_magnitude(2, 1) == 2, \
           "largest_magnitude: test case 1 failed"

    assert largest_magnitude(1, -2) == -2, \
           "largest_magnitude: test case 2 failed"
    assert largest_magnitude(-2, 1) == -2, \
           "largest_magnitude: test case 3 failed"

    assert largest_magnitude(-1, -2) == -2, \
           "largest_magnitude: test case 4 failed"
    assert largest_magnitude(-2, -1) == -2, \
           "largest_magnitude: test case 5 failed"

    assert largest_magnitude(0, 0) == 0, \
           "largest_magnitude: test case 6 failed"

    assert largest_magnitude(1, 1) == 1, \
           "largest_magnitude: test case 7 failed"
    assert largest_magnitude(-1, -1) == -1, \
           "largest_magnitude: test case 8 failed"
    
test_largest_magnitude()

