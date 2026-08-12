def add1Lon(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Adds 1 to each element of the list.
    Design Idea: Use structural recursion to process each element of the list.
    """
    if alon == []:
        return []
    else:
        return [alon[0] + 1] + add1Lon(alon[1:])

def test_add1Lon():
    """
    Signature: () -> None
    Purpose: Tests the add1Lon function
    Design Idea: Test list of different lengths and values.
    """
    assert add1Lon([]) == [], "Test 0 failed"
    assert add1Lon([0]) == [1], "Test 1 failed"
    assert add1Lon([1]) == [2], "Test 2 failed"
    assert add1Lon([1, 2, 3]) == [2, 3, 4], "Test 3 failed"
    assert add1Lon([-1, -2, -3]) == [0, -1, -2], "Test 4 failed"
    assert add1Lon([10, 20, 30]) == [11, 21, 31], "Test 5 failed"

test_add1Lon()

def doubleLon(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Doubles each element of the list.
    Design Idea: Use structural recursion to process each element of the list.
    """
    if alon == []:
        return []
    else:
        return [alon[0] * 2] + doubleLon(alon[1:])
    
def test_doubleLon():
    """
    Signature: () -> None
    Purpose: Tests the doubleLon function
    Design Idea: Test list of different lengths and values.
    """
    assert doubleLon([]) == [], "Test 0 failed"
    assert doubleLon([0]) == [0], "Test 1 failed"
    assert doubleLon([1]) == [2], "Test 2 failed"
    assert doubleLon([1, 2, 3]) == [2, 4, 6], "Test 3 failed"
    assert doubleLon([-1, -2, -3]) == [-2, -4, -6], "Test 4 failed"
    assert doubleLon([10, 20, 30]) == [20, 40, 60], "Test 5 failed"

test_doubleLon()

def add1Lon2(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Adds 1 to each element of the list.
    Design Idea: Use list comprehension to process each element of the list.
    """
    return [x + 1 for x in alon]

def test_add1Lon2():
    """
    Signature: () -> None
    Purpose: Tests the add1Lon2 function
    Design Idea: Test list of different lengths and values.
    """
    testvals = [[], [0], [1], [1, 2, 3], [-1, -2, -3], [10, 20, 30]]
    results = [[], [1], [2], [2, 3, 4], [0, -1, -2], [11, 21, 31]]
    for testval, result in zip(testvals, results):
        msg = f"add1Lon2: failed for {testval}"
        assert add1Lon2(testval) == result, msg

test_add1Lon2()

def doubleLon2(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Doubles each element of the list.
    Design Idea: Use list comprehension to process each element of the list.
    """
    return [x * 2 for x in alon]    

def test_doubleLon2():
    """
    Signature: () -> None
    Purpose: Tests the doubleLon2 function
    Design Idea: Test list of different lengths and values.
    """
    testvals = [[], [0], [1], [1, 2, 3], [-1, -2, -3], [10, 20, 30]]
    results = [[], [0], [2], [2, 4, 6], [-2, -4, -6], [20, 40, 60]]
    for testval, result in zip(testvals, results):
        msg = f"doubleLon2: failed for {testval}"
        assert doubleLon2(testval) == result, msg

test_doubleLon2()

def apply2all(f, alon):
    """
    Signature: (number -> number) (listof number) -> (listof number)
    Purpose: Applies function f to each element of the list.
    Design Idea: Use list comprehension to process each element of the list.
    """
    return [f(x) for x in alon]

def add1Lon3(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Adds 1 to each element of the list.
    Design Idea: Use apply2all to apply the add1 function to each element of the list.
    """
    return apply2all(lambda x: x + 1, alon)

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

def test_add1Lon3():
    """
    Signature: () -> None
    Purpose: Tests the add1Lon3 function
    Design Idea: Test list of different lengths and values.
    """
    test_funct(add1Lon3,\
    [[], [0], [1], [1, 2, 3], [-1, -2, -3], [10, 20, 30]],\
    [[], [1], [2], [2, 3, 4], [0, -1, -2], [11, 21, 31]])


test_add1Lon3()

def doubleLon3(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Doubles each element of the list.
    Design Idea: Use apply2all to apply the double function to each element of the list.
    """
    return apply2all(lambda x: x * 2, alon)

def test_doubleLon3():
    """
    Signature: () -> None
    Purpose: Tests the doubleLon3 function
    Design Idea: Test list of different lengths and values.
    """
    test_funct(doubleLon3, \
    [[], [0], [1], [1, 2, 3], [-1, -2, -3], [10, 20, 30]],\
    [[], [0], [2], [2, 4, 6], [-2, -4, -6], [20, 40, 60]])

test_doubleLon3()

def add1Lon4(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Adds 1 to each element of the list.
    Design Idea: Use map to apply the add1 function to each element of the list.
    """
    return list(map(lambda x: x + 1, alon))

def test_add1Lon4():
    """
    Signature: () -> None
    Purpose: Tests the add1Lon4 function
    Design Idea: Test list of different lengths and values.
    """
    test_funct(add1Lon4, [[], [0], [1], [1, 2, 3], [-1, -2, -3], [10, 20, 30]], [[], [1], [2], [2, 3, 4], [0, -1, -2], [11, 21, 31]])

test_add1Lon4()

def doubleLon4(alon):
    """
    Signature: (listof number) -> (listof number)
    Purpose: Doubles each element of the list.
    Design Idea: Use map to apply the double function to each element of the list.
    """
    return list(map(lambda x: x * 2, alon))

def test_doubleLon4():
    """
    Signature: () -> None
    Purpose: Tests the doubleLon4 function
    Design Idea: Test list of different lengths and values.
    """
    test_funct(doubleLon4, [[], [0], [1], [1, 2, 3], [-1, -2, -3], [10, 20, 30]], [[], [0], [2], [2, 4, 6], [-2, -4, -6], [20, 40, 60]])

test_doubleLon4()

