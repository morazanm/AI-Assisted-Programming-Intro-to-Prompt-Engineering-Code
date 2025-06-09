"""
An evenlon is either:
  1. []
  2. [number] + [number] + lon

A 2lon is [number, number], where the first number is less than or equal to the second number.

Template for functions on a 2lon:
def f_on_2lon(a2lon ...):
    Signature: 2lon ... -> ...
    Purpose: 
    Design Idea:
    <combine f_on_number(a2lon[0]) f_on_number(a2lon[1])>

def test_f_on_2lon():
    Signature: -> None
    Purpose: test f_on_2lon
    Design Idea: Test 2lon with random numbers

    assert f_on_2lon(<2lon>, ...) == ..., "Test 0 failed"
    assert f_on_2lon(<2lon>, ...) == ..., "Test 1 failed"
    assert f_on_2lon(<2lon>, ...) == ..., "Test 2 failed"
    .
    .
    .

test_f_on_2lon()

A 2lonList is either:
  1. []
  2. 2lon + 2lonList

Tempate for functions on a 2lonList:

def f_on_2lonList(a2lonlst ...):
    Siganture: 2lonList ... -> ...
    Purpose: 
    Design Idea:
    if a2lonList == []:
        return <base case value>
    else:
        return <combine f_on_2lon(a2lonlst[0]) f_on_2lonList(a2lonlst[1:])>

def test_f_on_2lonList():
    Signature: -> None
    Purpose: test f_on_2lon
    Design Idea: Test empty and nonempty 2lonList

    assert f_on_2lon([], ...) == <base case value>, "Test 0 failed
    assert f_on_2lon(a2lonList, ...) == ..., "Test 1 failed"
    .
    .
    .

test_f_on_2lon()
"""
def evenlonTo2lonList(evlon):
    """
    Signature: evenlon -> 2lonList
    Purpose: Convert an evenlon to a 2lonList
    Design Idea: If given evenlon is empty, return empty 2lonList.
                 If the first two elements of the evenlon are in order,
                   construct a 2lon containing the first element followed 
                   by the second element and append the 2lonList obtained 
                   by recursively processing the rest of the elements, 
                   not including the first two, of the given evenlon.
                 If the first two elements of the given evenlon are not 
                 in order, construct a 2lon containing the second element 
                 followed by the first element and append the 2lonList 
                 obtained by recursively processing the rest of the 
                 elements, not including the first two, of the given 
                 evenlon.
    """
    if evlon == []:
        return []
    elif evlon[0] <= evlon[1]:
        return [[evlon[0]] + [evlon[1]]] + evenlonTo2lonList(evlon[2:])
    else:
        return [[evlon[1]] + [evlon[0]]] + evenlonTo2lonList(evlon[2:])
    # Termination argument:
    # evlon has an even number of elements. Every recursive call
    # removes two elements from evlon, so the number of elements
    # in evlon decreases by 2 and its length remains even. 
    # Eventually, evlon become empty and the recursion stops.

def test_evenlonTo2lonList():
    """
    Signature: -> None
    Purpose: test evenlonTo2lonList
    Design Idea: Test empty and nonempty evenlons with random numbers
    """
    assert evenlonTo2lonList([]) == [], "Test case 0 failed"
    assert evenlonTo2lonList([1, 2]) == [[1, 2]], "Test case 1 failed"
    assert evenlonTo2lonList([2, 1]) == [[1, 2]], "Test case 2 failed"
    assert evenlonTo2lonList([1, 3, 2, 4]) == [[1, 3], [2, 4]], "Test case 3 failed"
    assert evenlonTo2lonList([3, 1, 4, 2]) == [[1, 3], [2, 4]], "Test case 4 failed"
    assert evenlonTo2lonList([5, 6, 7, 8]) == [[5, 6], [7, 8]], "Test case 5 failed"
    assert evenlonTo2lonList([8, 7, 6, 5]) == [[7, 8], [5, 6]], "Test case 6 failed"

test_evenlonTo2lonList()



    