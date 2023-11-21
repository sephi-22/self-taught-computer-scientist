# A factorial function that is iterative.
def factorial_iterative(number):
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    print("The factorial (iterative) is:", fact)


factorial_iterative(4)


# A factorial function that is recursive.
def factorial_recursive(number):
    if number < 2:  # Base Case
        return 1
    return number * factorial_recursive(number - 1)  # Recursive Case


print("The factorial (recursive) is:", factorial_recursive(5))


# Function to print numbers from 1 to 10 recursively
def print_numbers(n=1):
    if n <= 10:
        print(n)
        print_numbers(n + 1)


print_numbers()
