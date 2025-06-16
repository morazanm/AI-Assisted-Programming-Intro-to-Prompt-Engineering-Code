import testfunct
from functools import reduce

def findMax1(alon):
    """
    Signature: (listof number) -> number
    Purpose: Find the maximum value in the list.
    Design Idea: Accumulate the max as the list is traversed
    Assumption: The alon is not empty.
    """

    def helper(lst, acc):
        """
        Signature: (listof number) number -> number
        Purpose: Helper function to find the maximum value in the list.
        Design Idea: Accumulate the max in the proccessed part of alon
        Accumulator Invariant:
          acc = max(alon-lst)
        """
        if alon == []:
            return acc
        else:
            return helper(alon[1:], max(acc, alon[0]))

    helper(alon, float('-inf')  )

def test_findMax1():
    """
    Signature: () -> None
    Purpose: Test findMax
    Design Idea: Test findMax with different (listof number)
    """
    testfunct.test_funct(findMax1, 
                         [[1, 2, 3],[-3,2,-10],[-14,-33,-25],[0]], 
                         [3, 2, -14, 0])

def findMax(alon):
    """
    Signature: (listof number) -> number
    Purpose: Find the maximum value in the list.
    Design Idea: Use reduce to find the maximum value in the list.
    Accumulator Invariant:
          acc = max(alon-lst)
    Assumption: The list is not empty.
    """
    return reduce(lambda x, acc: max(x, acc), alon, float('-inf'))

def test_findMax():
    """
    Signature: () -> None
    Purpose: Test findMax
    Design Idea: Test findMax with different (listof number)
    """
    testfunct.test_funct(findMax, 
                         [[1, 2, 3],[-3,2,-10],[-14,-33,-25],[0]], 
                         [3, 2, -14, 0])

def fact(n):
    """
    Signature: natnum -> natnum
    Purpose: Compute n!
    Design Idea: Reduce the interval [0..n] to n!
    Accumulator Invariant:
        acc = product of the numbers in, [0..i], the processed part of interval [1..n+1)
    """
    return reduce(lambda x, acc: x * acc, range(1, n + 1), 1)

def test_fact():
    """
    Signature: test_fact : () -> ()
    Purpose: Test fact
    Design Idea: Test fact with different natnums
    """
    testfunct.test_funct(fact, [0,1,2,3,8,10], [1,1,2,6,40320,3628800])

test_fact()

