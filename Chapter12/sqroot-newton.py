import decimal

dplaces = 70
decimal.getcontext().prec = dplaces
TOL = decimal.Decimal(10**-50)

def sqroot(approx, a):
    HALF = decimal.Decimal(1/2)
    """
    Signature: decimal.Decimal decimal.Decimal -> decimal.decimal
    Purpose: Approximate the square root of the given nuber using the Newton-Rapson method
    Design Idea:
      Represent numbers using decimal.Decimal
      If abs(approx^2 - a) < TOL return approx
      otherwise, recursively process HALF*(approx + a/approx) and a
    """
    if abs(approx**2 - a) < TOL:
        return approx
    else:
        return sqroot(HALF * (approx + a / approx), a)
    """
    Termination argument:
      Every recusive call generates a better approximation for the aquare root
      of a. Assuming that the maximum number of recursive calls is not reached,
      the square of the approximation will eventually be within TOL of a and the
      function halts.
    """
    
def test_sqroot():
    """
    Signature:  -> None
    Purpose: Test sqroot
    Design Idea: 
      Use decimal.Decimal to represent numbers
      For the tests:
        use 0, 16, 49, 2, 3, and 10 for a
        use 3, 1, 4, 20, 11, and 100 for approx
      The square of the result from calling sqroot should be within  of the square of the tested integer
      Use assert to check the result
      Include failed test strings "Test n failed" where n in [0..5]
    """
    for i, a in enumerate([0, 16, 49, 2, 3, 10]):
        for approx in [3, 1, 4, 20, 11, 100]:
            result = sqroot(decimal.Decimal(approx), decimal.Decimal(a))
            assert abs(result**2 - decimal.Decimal(a)) < TOL, f"Test {i} failed"

test_sqroot()

for n in [0, 16, 49, 2, 3, 10]:
    print(f"sqroot({n}) = {sqroot(decimal.Decimal(1), decimal.Decimal(n))} sq is {sqroot(decimal.Decimal(1), decimal.Decimal(n))**2}")


    
    
#print(sqroot(decimal.Decimal(1),decimal.Decimal(2)))
