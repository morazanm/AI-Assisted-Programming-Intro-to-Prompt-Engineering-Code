
def double(n):
    """
    Signature: number -> number
    Purpose: Returns the double of the input number.
    Design Idea: Multiply the input number by 2.
    """
    return n * 2

def quadruple(n):
    """
    Signature: number -> number
    Purpose: Returns the quadruple of the input number
    Design Idea: Add the double of the input number to itself
    """
    return double(n) + double(n)

print(quadruple(None))