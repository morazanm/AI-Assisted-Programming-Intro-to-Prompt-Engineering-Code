from mpmath import mp, sqrt, pi

def computePi(n, decplaces):
    mp.dps = decplaces
    amean = mp.one
    gmean = mp.one/sqrt(2)
    scalefactor = mp.one
    approx = mp.one/4

    for _ in range(n):
        old_amean = amean
        amean = (amean+gmean)/2
        gmean = sqrt(amean*gmean)
        approx = approx - scalefactor*(old_amean-amean)**2
        scalefactor = 2*scalefactor
    return((amean+gmean)**2 / (4*approx))


    

def calculate_pi_agm(iterations, precision):
    """
    Calculates Pi using the Gauss-Legendre algorithm based on the AGM.

    Args:
        iterations (int): The number of iterations for the algorithm.
        precision (int): The number of decimal places for the calculation.

    Returns:
        mpf: The calculated value of Pi.
    """
    mp.dps = precision  # Set the desired decimal precision

    a = mp.one
    b = 1 / sqrt(2)
    t = mp.one / 4
    p = mp.one

    for _ in range(iterations):
        a_next = (a + b) / 2
        b_next = sqrt(a * b)
        t_next = t - (p * (a - a_next)**2)
        p_next = 2 * p

        a, b, t, p = a_next, b_next, t_next, p_next

    return (a + b)**2 / (4 * t)

# Example usage:
num_iterations = 100  # Number of iterations
decimal_places = 50  # Desired decimal places of Pi

calculated_pi  = computePi(num_iterations, decimal_places)
calculated_pi2 = computePi(num_iterations, decimal_places)
print(f"Calculated Pi : {calculated_pi}")
print(f"Calculated Pi2: {calculated_pi2}")
print(f"Actual Pi (mpmath): {pi}")