def scaleList(alon, scalar):
    """
    Signature: (listof number) number -> (listof number)
    Purpose: Scale the given lon by the given scalar.
    Design Idea: map a function that multiplies its argument by the scalar
    """
    scaleHelper = lambda x: x * scalar
    return list(map(scaleHelper, alon))

def test_scaleList():
    """
    Signature: () -> None
    Purpose: Test the scaleList function.
    Design Idea: Test using lons with varying lengths and values.
    """
    assert scaleList([1, 2, 3], 2) == [2, 4, 6]
    assert scaleList([0, -1, -2], 3) == [0, -3, -6]
    assert scaleList([], 5) == []
    assert scaleList([-1, 0, 1], -2) == [2, 0, -2]

test_scaleList()
