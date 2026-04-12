
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
                 3. a golden rectangle with lengths 8.0901699 and 5
                 4. several golden rectangles with lengths 8.0901699*k and 5*k, where k=3,44,87
                 5. non-golden rectangles
                 Include fail test strings starting at 0
    """
    # Test golden rectangles with 1.6180339887 and 1
    test_case = 0
    for k in [1, 5, 11, 31]:
        assert goldenRect(1.6180339887 * k, 1 * k) == True, f"Test case {test_case} failed"
        test_case += 1

    # Test golden rectangles with 8.0901699 and 5
    for k in [1, 3, 44, 87]:
        assert goldenRect(8.0901699 * k, 5 * k) == True, f"Test case {test_case} failed"
        test_case += 1

    # Non-golden rectangles
    non_golden_cases = [(2, 1), (3, 2), (4, 3)]
    for larger, smaller in non_golden_cases:
        assert goldenRect(larger, smaller) == False, f"Test case non-golden rectangle ({larger},{smaller}) failed"





   

test_goldenRect()





    