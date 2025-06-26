"""
Template for generative recursion

def genrecf(prob ...):
    ;; Signature: ... -> ...
    ;; Purpose: 
    Design idea: 
    How-statement: 
    if base_case1:
        return base_case1_value
    elif base_case2:
        return base_case2_value
    .
    .
    .
    elif base_caseN:
        return base_caseN_value
    else:
        return <combine genrecf(subproblem1 ...)
                        genrecf(subproblem2 ...)
                        .
                        .
                        .
                        genrecf(subproblemN ...)>
    ;; Termination argument:

def test_genrecf():
    ;; Signature: -> None
    ;; Purpose:  Test the function genrecf with ... 
    assert genrecf(<problem instance> ...) == ...
    assert genrecf(<problem instance> ...) == ...
    .
    .
    .

A range, R=[start,end], is either:
  1. [ ], when start > end
  2. [R[start:end-1], end]
"""
def gcd_helper(larger, smaller, rng):
    """
    Signature: natnum natnum range -> natnum
    Purpose: Compute the greatest common divisor of a and b
    Design idea: Find largest common divisor of a and b in rng.
    """
    if larger%rng[0]==0 and smaller%rng[0]==0:
        return rng[0]
    else:
        return gcd_helper(larger, smaller, rng[1:])

def gcd(a, b):
    """
    Signature: natnum>=1 natnum>=1 -> natnum>=1
    Purpose: Compute the greatest common divisor of a and b
    Design idea: Find largest common divisor of a and b in [1..a].
    """
    return gcd_helper(max(a, b), min(a, b), range(min(a,b), 0, -1))

def test_gcd():
    """
    Signature: -> None
    Purpose: Test gcd function
    Design idea: Test with several pairs of numbers that:
                   have and do not have 1 as their gcd
                   have the smaller number as the first argument
                   have the larger number as the first argument
    """
    assert gcd(12, 15) == 3, "Test case 0 failed"
    assert gcd(18, 6) == 6, "Test case 1 failed"
    assert gcd(45, 60) == 15, "Test case 2 failed"
    assert gcd(23, 17) == 1, "Test case 3 failed"
    assert gcd(1, 8) == 1, "Test case 4 failed"
    assert gcd(1, 1) == 1, "Test case 5 failed"
    assert gcd(101135853, 45014640) == 177, "Test case 6 failed"

test_gcd()

def lame_helper(larger, smaller):
    """
    Signature: natnum natnum -> natnum
    Purpose: Compute the greatest common divisor of a and b using lame's algorithm
    Design idea: Use the property that gcd(a, b) = gcd(b, a % b)
    Assumption: larger >= smaller
    """
    if smaller == 0:
        return larger
    else:
        return lame_helper(smaller, larger % smaller)
    """
    Termination argument: Every recursive call makes brings
    smaller closer to 0. Eventually, smaller becomes 0, and the
    function terminates
    """

def gcd_lame(a, b):
    """
    Signature: natnum>=1 natnum>=1 -> natnum>=1
    Purpose: Compute the greatest common divisor of a and b using lame's algorithm
    Design idea: Use the property that gcd(a, b) = gcd(b, a % b)
    """
    if a<=b:
        return lame_helper(b, a)
    else:
        return lame_helper(a, b)
    
def test_gcd_lame():
    """
    Signature: -> None
    Purpose: Test gcd_lame function
    Design idea: Test with several pairs of numbers that:
                   have and do not have 1 as their gcd
                   have the smaller number as the first argument
                   have the larger number as the first argument
    """
    assert gcd_lame(12, 15) == 3, "Test case 0 failed"
    assert gcd_lame(18, 6) == 6, "Test case 1 failed"
    assert gcd_lame(45, 60) == 15, "Test case 2 failed"
    assert gcd_lame(23, 17) == 1, "Test case 3 failed"
    assert gcd_lame(1, 8) == 1, "Test case 4 failed"
    assert gcd_lame(1, 1) == 1, "Test case 5 failed"
    assert gcd_lame(101135853, 45014640) == 177, "Test case 6 failed"

test_gcd_lame()

#print(gcd(101135853, 45014640))
#print(gcd_lame(101135853, 45014640))