"""
Data Definition
A natural number, natnum, is either:
  1. 0
  2. n+1, where n is a natnum

Template for a function on a natnum

def f_on_natnum(n, ...)
    Signature: natnum ... -> ...
    Purpose: 
    Design Idea:
    if (n == 0):
        return < base case value >
    else :
        return < combine n f_on_natnum (n -1 , ...)

def test_f_on_natnum ():
    Signature: -> None
    Purpose: Test f_on_natnum
    Design idea:
    assert f_on_natnum (0 , ...)==... , " Test 0 failed "
    assert f_on_natnum (1 , ...)==... , " Test 1 failed "
    assert f_on_natnum (2 , ...)==... , " Test 2 failed "
    .
    .
    .
test_f_on_natnum ()
"""

def tri(n):
    """
    Signature: natnum -> natnum
    Purpose: Compute the nth triangular number
    Design Idea:
      Use the closed-form formula: n * (n + 1) // 2
    """
    return n * (n + 1) // 2

def test_tri():
    """
    Signature: -> None
    Purpose: Test tri
    Design Idea: Use different natural numbers for testing
    """
    assert tri(0) == 0, "Test 0 failed"
    assert tri(1) == 1, "Test 1 failed"
    assert tri(2) == 3, "Test 2 failed"
    assert tri(3) == 6, "Test 3 failed"
    assert tri(4) == 10, "Test 4 failed"
    assert tri(5) == 15, "Test 5 failed"

test_tri()

def tetra(n):
    """
    Signature: natnum -> natnum
    Purpose: Compute the nth tetrahedral number
    Design Idea:
      Use the closed-form formula: n * (n + 1) * (n + 2) // 6
    """
    return n * (n + 1) * (n + 2) // 6
    
def test_tetra():
    """
    Signature: -> None
    Purpose: Test tetra
    Design Idea: Use different natural numbers for testing
    """
    assert tetra(0) == 0, "Test 0 failed"
    assert tetra(1) == 1, "Test 1 failed"
    assert tetra(2) == 4, "Test 2 failed"
    assert tetra(3) == 10, "Test 3 failed"
    assert tetra(4) == 20, "Test 4 failed"
    assert tetra(5) == 35, "Test 5 failed"

test_tetra()

