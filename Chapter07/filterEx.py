import testfunct

def getStrings1(alist):
    """
    Signature: (listof X) -> (listof str)
    Purpose: Extract the strings in alist
    Design Idea: As the list is traversed, the string elements are added to the result
    """
    if alist == []:
        return []
    elif isinstance(alist[0], str):
        return [alist[0]] + getStrings1(alist[1:])
    else:
        return getStrings1(alist[1:])

def test_getStrings1():
    """
    Signature: () -> None
    Purpose: Test the getStrings function
    Design Idea: Use testfunct to test the getStrings function
    """
    testfunct.test_funct(getStrings1,\
                         [[], [1, 2, 3], [1, "a", 2, "AIPD", 3], \
                           [44, True, None, "MTM", ["b", "c"]]],\
                         [[], [], ["a", "AIPD"], ["MTM"]])

test_getStrings1()

def getStrings(alist):
    """
    Signature: (listof X) -> (listof str)
    Purpose: Extract the strings from the given list
    Design Idea: Use filter extract the strings from the given list
    """
    return list(filter(lambda x: isinstance(x, str), alist))

def test_getStrings():
    """
    Signature: () -> None
    Purpose: Test the getStrings function
    Design Idea: Use testfunct to test the getStrings function
    """
    testfunct.test_funct(getStrings,\
                         [[], [1, 2, 3], [1, "a", 2, "AIPD", 3], \
                           [44, True, None, "MTM", ["b", "c"]]],\
                         [[], [], ["a", "AIPD"], ["MTM"]])

test_getStrings()

