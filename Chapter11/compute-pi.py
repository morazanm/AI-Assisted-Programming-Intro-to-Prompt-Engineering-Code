import decimal
import math

decimal.getcontext().prec = 50

def fact(n):
    res = 1
    k = 0
    while k<n:
        k = k + 1
        res = res * k
    return(res)

def NewtonSqrt(x, initapprox):
    LIM = decimal.Decimal(10**10)
    TOL = 1/LIM
    approx = initapprox

    while abs((approx**2) - x) > TOL:
        approx = (approx + (x/approx))/2
    return(approx)

    



def ChudnovskySum(f, iterations):
    k = 0
    asum = 1
    bsum = 0

    while k<iterations:
        k = k + 1
        ak = f(k) 
        asum = asum + ak
        bsum = bsum + (ak * k)
    return((asum, bsum))

def ChudnovskyPi_v0(iterations):
    numerator = 426880*math.sqrt(10005)
    afactor = 13591409
    bfactor = 545140134
    t = ChudnovskySum(lambda k: ((-1**k)*(fact(6*k)))/(fact(3*k)*(fact(k)**3)*(640320**(3*k))), iterations)
    return(numerator/(afactor*t[0] + bfactor*t[1]))

def ChudnovskyPi_v1(iterations):
    numerator = 426880*math.sqrt(10005)
    afactor = 13591409
    bfactor = 545140134
    t = ChudnovskySum(lambda k: (24 * (6*k - 5) * (2*k - 1) * (6*k - 1))/(640320**3 * k**3), iterations)
    return(numerator/(afactor*t[0] + bfactor*t[1]))

def ChudnovskyPi_v2(iterations):
    numerator = 426880*math.sqrt(10005)
    afactor = 13591409
    bfactor = 545140134
    t = ChudnovskySum(lambda k: (24 * (6*k - 5) * (2*k - 1) * (6*k - 1))/(640320**3 * k**3), iterations)
    return(numerator/(afactor*t[0] + bfactor*t[1]))

print(ChudnovskyPi_v0(3))
print(ChudnovskyPi_v1(3))
print(ChudnovskyPi_v2(3))
print("")
print(NewtonSqrt(2, 1))

