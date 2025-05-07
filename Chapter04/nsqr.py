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

def addktimes(n, k):
    """
    Signature: natnum natnum -> natnum
    Purpose: Compute n*k
    Design idea: Add n to 0 k times
    """
    if k == 0:
        return 0
    else:
        return n + addktimes(n, k-1)

def test_addktimes():
    """
    Signature: -> None
    Purpose: Test add_ktimes
    Design idea: Test the function with 0 and nonzero natnums for k and differnent natnums for n
    """
    assert addktimes(0,0) == 0, "Test 0 failed"
    assert addktimes(0,20) == 0, "Test 1 failed"
    assert addktimes(2,6) == 12, "Test 2 failed"
    assert addktimes(3,3) == 9, "Test 3 failed"
    assert addktimes(7,4) == 28, "Test 4 failed"

test_addktimes()

def nsqr(n):
    """
    Signature: natnum -> natnum
    Purpose: Return the square of n
    Design idea: Add n to 0 n times
    """
    return addktimes(n, n)

def test_nsqr():
    """
    Signature: -> None
    Purpose: Test nsqr
    Design idea: Test the function with 0 and nonzero natnums
    """
    assert nsqr(0) == 0, "nsqr: Test 0 failed"
    assert nsqr(1) == 1, "nsqr: Test 1 failed"
    assert nsqr(2) == 4, "nsqr: Test 2 failed"
    assert nsqr(3) == 9, "nsqr: Test 3 failed"
    assert nsqr(4) == 16, "nsqr: Test 4 failed"

test_nsqr()
