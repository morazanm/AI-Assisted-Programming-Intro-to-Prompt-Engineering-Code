import testfunct

def add1Lon(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Adds 1 to each element of the list.
    Design Idea: Use map to apply the add1 function to each element of the list.
    """
    return list(map(lambda x: x + 1, alon))

def test_add1Lon():
    """
    Signature: () -> None
    Purpose: Tests the add1Lon4 function
    Design Idea: Test list of different lengths and values.
    """
    testfunct.test_funct(add1Lon, [[], [0], [1], [1, 2, 3], [-1, -2, -3], [10, 20, 30]],\
                         [[], [1], [2], [2, 3, 4], [0, -1, -2], [11, 21, 31]])

test_add1Lon()

def doubleLon(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Doubles each element of the list.
    Design Idea: Use map to apply the double function to each element of the list.
    """
    return list(map(lambda x: x * 2, alon))

def test_doubleLon():
    """
    Signature: () -> None
    Purpose: Tests the doubleLon4 function
    Design Idea: Test list of different lengths and values.
    """
    testfunct.test_funct(doubleLon, [[], [0], [1], [1, 2, 3], [-1, -2, -3], [10, 20, 30]],\
                          [[], [0], [2], [2, 4, 6], [-2, -4, -6], [20, 40, 60]])

test_doubleLon()

def sqrEvens(n):
    """
    Signature: natnum -> (listof natnum)
    Purpose: Square the even numbers from 0 to n.
    Design Idea: Use map to apply a square function to each even natnum in the interval
    """
    if n % 2 == 0:
        return list(map(lambda x: x ** 2, range(0,n+1,2)))
    else:
        return list(map(lambda x: x ** 2, range(0,n,2)))

def test_sqrEvens():
    """
    Signature: () -> None
    Purpose: Tests the sqrEvens function
    Design Idea: Test using different natnum.
    """
    testfunct.test_funct(sqrEvens, 
                         [0, 1, 2, 3, 4], 
                         [[0], [0], [0, 4], [0, 4], [0, 4, 16]])
    
test_sqrEvens()
