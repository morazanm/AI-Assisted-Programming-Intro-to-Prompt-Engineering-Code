
def goldenRect(larger, smaller):
    goldenratio = (1 + 5**0.5)/2
    """
    Signature: number number -> Boolean
    Purpose: Determine if the given lengths are for a golden rectangle
    Design Idea: Determine if larger/smaller==goldenRatio
    Assumption: large > 0, smaller > 0, and larger > smaller
    """
    # Check if the ratio is approximately equal to the golden ratio
    epsilon = 1e-5
    return abs((larger / smaller) - goldenratio) < epsilon

def test_goldenRect():
    """
    Signature: -> None
    Purpose: Test the goldenRect function
    Design Idea: Test the following cases:
                 1. a golden rectangle with lengths 1.6180339887 and 1
                 2. several golden rectangles with lengths 1.6180339887*k and 1*k, where k=5,11,31
                 3. a golden rectangle with lengths 8.0901699 and 5, where k>0
                 4. several golden rectangles with lengths 8.0901699*k and 5*k, where k=3,44,87
                 5. non-golden rectangles
                 Include fail test strings starting at 0
    """
    assert goldenRect(1.6180339887, 1) == True, "Test case 0 failed"
    assert goldenRect(1.6180339887 * 5, 1 * 5) == True, "Test case 1 failed"
    assert goldenRect(1.6180339887 * 11, 1 * 11) == True, "Test case 2 failed"
    assert goldenRect(1.6180339887 * 31, 1 * 31) == True, "Test case 3 failed"
    assert goldenRect(8.09, 5) == True, "Test case 4 failed"
    assert goldenRect(8.09 * 3, 5 * 3) == True, "Test case 5 failed"
    assert goldenRect(8.09 * 44, 5 * 44) == True, "Test case 6 failed"
    assert goldenRect(8.09 * 87, 5 * 87) == True, "Test case 7 failed"
    
    # Non-golden rectangles
    assert goldenRect(2, 1) == False, "Test case non-golden rectangle (2,1) failed"
    assert goldenRect(3, 2) == False, "Test case non-golden rectangle (3,2) failed"
    assert goldenRect(4, 3) == False, "Test case non-golden rectangle (4,3) failed"





   

test_goldenRect()





    