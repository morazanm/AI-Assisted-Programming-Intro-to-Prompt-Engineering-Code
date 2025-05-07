"""
Data Definition
  A natnum is either:
    1. 0
    2. n+1, where n is a natnum

Function Template

def f_on_natnum(n, ...):
    Signature: natnum ... -> ...
    Purpose:
    Design idea: 
    if n == 0:
        return <base case value>
    else:
        return <combine n f_on_natnum(n-1, ...)

def test_f_on_natnum():
    Signature:  -> None
    Purpose: Test f_on_natnum
    Design idea: ...
    assert f_on_natnum(0, ...)==..., "Test 0 failed"
    assert f_on_natnum(1, ...)==..., "Test 1 failed"
    assert f_on_natnum(2, ...)==..., "Test 2 failed"
    ...
"""

def sumfirstNsquares(n):
    """
    Signature: natnum -> natnum
    Purpose: Compute the sum of the first n squares.
    Design idea: Use structural recursion on n.
    """
    if n == 0:
        return 0
    else:
        return n * n + sumfirstNsquares(n - 1)

def test_sumfirstNsquares():
    """
    Signature:  -> None
    Purpose: Test sumfirstNsquares
    Design idea: Test the function with 0 and other natural numbers.
    """
    assert sumfirstNsquares(0) == 0, "Test 0 failed"
    assert sumfirstNsquares(1) == 1, "Test 1 failed"
    assert sumfirstNsquares(2) == 5, "Test 2 failed"
    assert sumfirstNsquares(3) == 14, "Test 3 failed"
    assert sumfirstNsquares(4) == 30, "Test 4 failed"
    assert sumfirstNsquares(10) == 385, "Test 5 failed"
    assert sumfirstNsquares(100) == 338350, "Test 6 failed"

test_sumfirstNsquares()

def archimedesFormula(n):
    """
    Signature: natnum -> natnum
    Purpose: Compute the value of Archimedes formula n(n+1)(2n+1)/6
    Design idea: Plug in the value of n into the formula
    """
    return (n * (n + 1) * (2 * n + 1)) / 6

def test_archimedesFormula():
    """
    Signature:  -> None
    Purpose: Test achimedesFormula
    Design idea: Test the function with 0 and other natural numbers.
    """
    assert archimedesFormula(0) == 0, "Test 0 failed"
    assert archimedesFormula(1) == 1, "Test 1 failed"
    assert archimedesFormula(2) == 5, "Test 2 failed"
    assert archimedesFormula(3) == 14, "Test 3 failed"
    assert archimedesFormula(4) == 30, "Test 4 failed"
    assert archimedesFormula(10) == 385, "Test 5 failed"
    assert archimedesFormula(100) == 338350, "Test 6 failed"

test_archimedesFormula()

def holdsArchimedes(n):
    """
    Signature: natnum -> Boolean
    Purpose: Determine if Archimedes formula the sum of the first n squares holds.
    Design idea: Test the sum of the first n squares against for equality with n(n+1)(2n+1)/6
    """
    return sumfirstNsquares(n) == archimedesFormula(n)

def test_holdsArchimedes():
    """
    Signature:  -> None
    Purpose: Test holdsArchimedes
    Design idea: Test the function with a few values of n.
    """
    assert holdsArchimedes(0) == True, "Test 0 failed"
    assert holdsArchimedes(1) == True, "Test 1 failed"
    assert holdsArchimedes(2) == True, "Test 2 failed"
    assert holdsArchimedes(3) == True, "Test 3 failed"
    assert holdsArchimedes(4) == True, "Test 4 failed"
    assert holdsArchimedes(10) == True, "Test 5 failed"

test_holdsArchimedes()