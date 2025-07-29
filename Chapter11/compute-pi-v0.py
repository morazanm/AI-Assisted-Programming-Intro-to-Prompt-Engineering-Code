import math
import decimal

dplaces = 50
decimal.getcontext().prec = dplaces
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

def fact (n):
    """
    Signature: natnum -> decimal.Decimal
    Purpose: Compute n!
    Design Idea: 
      Start an accumulator for the result at 1
      Loop through k = 1 to n, multiplying the accumulator by each value of k
    Loop Invariant:
      res = k! and k<=n
    """
    res = decimal.Decimal(1)
    # Hoare Logic assertion: {res == 1 and assume k == 0}
    for k in range(1, n + 1):
        # Hoare Logic assertion: {res == (k-1)! before iteration}
        res *= decimal.Decimal(k)
        # Hoare Logic assertion: {res == k! after iteration}
    # Hoare Logic assertion: {res == n!}
    return res

def test_fact():
    """
    Signature: -> None
    Purpose: Test fact
    Design Idea:
      Use different values of n to test fact
      Include fail test strings "Test n failed" starting with n=0,1,2,3,...
    """
    assert fact(0) == decimal.Decimal(1), "Test 0 failed"
    assert fact(1) == decimal.Decimal(1), "Test 1 failed"
    assert fact(2) == decimal.Decimal(2), "Test 2 failed"
    assert fact(3) == decimal.Decimal(6), "Test 3 failed"
    assert fact(4) == decimal.Decimal(24), "Test 4 failed"
    assert fact(5) == decimal.Decimal(120), "Test 5 failed"


def ChudnovskySum(f, iterations):
    """ 
    Signature: (natnum -> decimal.Decimal) natnum -> decimal.Decimal
    Purpose: Compute the series from 0 to the given number of iterations
    Design Idea: 
      Represent numbers using decimal.Decimal for high precision
      Add the terms of the series produced by f
      Use structural recurion on iterations to compute the sum
      Structure the code using the template for a function on a natnum
      When iterations is 0, return 13591409. Otherwise, add the next term to the sum of the rest of the terms
    """
    if iterations == 0:
        return decimal.Decimal(13591409)
    else:
        return f(iterations) + ChudnovskySum(f, iterations - 1)
    

def computePi(iterations):
    """
    Signature: natnum -> decimal.Decimal
    Purpose: Approximate the value of pi
    Design Idea:
       Represent numbers using decimal.Decimal for high precision
       Use the following variables and function:
         k = sqrt(10005)/4270934400
         f = (−1^k * fact(6k) * (13591409+545140134k))/(fact(3k) * fact(k)^3 * 640320^3k)
         ChudnovskySum(f, iterations) to compute the series
       return 1/(k * series)
    """
    k = decimal.Decimal(math.sqrt(10005)) / decimal.Decimal(4270934400)
    f = lambda k: (decimal.Decimal((-1) ** k) * fact(6 * k) *
                   (decimal.Decimal(13591409) + decimal.Decimal(545140134) * k)) / \
                   (fact(3 * k) * (fact(k) ** 3) * (decimal.Decimal(640320) ** (3 * k)))
    series = ChudnovskySum(f, iterations)
    return 1 / (k * series)

def test_computePi():
    """
    Signature: -> None
    Purpose: Test computePi
    Design Idea:
      Define Pi as a Decimal('3.14159265358979323846264338327950288419716939937510')
      define a tolerance equal to 10**-15
      Use iterations = multiples of 50 in [1, 1000]
      Include fail test strings "Test n failed" where n is the input to computePi.
    """
    Pi = decimal.Decimal('3.14159265358979323846264338327950288419716939937510')
    tolerance = decimal.Decimal(10) ** -10
    for n in range(1, 1000, 50):
        computed_pi = computePi(n)
        assert abs(computed_pi - Pi) < tolerance, f"Test {n} failed"
    
test_computePi() 

