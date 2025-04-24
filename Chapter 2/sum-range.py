def sum_range(a,b):
    result = 0
    for i in range(a, b+1):
        result = result + i
    return result

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number >= to the first: "))
    print(f"The sum of the range from {a} to {b} is {sum_range(a,b)}")

main()