def scaleList(L, scalar):
    """
    Signature: (listof number) number -> (listof number)
    Purpose: Scale the given list by the given scalar.
    Design Idea: Use an accumulator to scale the given list.
    """
    def scaleListHelper(lst, acc):
        if lst == []:
            return acc
        else:
            return scaleListHelper(lst[1:], acc+ [(lst[0]*scalar)])
    return scaleListHelper(L, [])

def test_scaleList():
    """
    Signature: () -> None
    Purpose: Test the scaleList function.
    Design Idea: Use lons of different lengths and values with different scalars.
    """
    assert scaleList([], 2) == [], "Test case 0 failed"
    assert scaleList([1], 2) == [2], "Test case 1 failed"
    assert scaleList([1, 2, 3], 2) == [2, 4, 6], "Test case 2 failed"
    assert scaleList([1, 2, 3], 0) == [0, 0, 0], "Test case 3 failed"
    assert scaleList([1, 2, 3], -1) == [-1, -2, -3], "Test case 4 failed"

test_scaleList()

def times(x, y, z):
    return x * y * z

print(times(10,20,3))
