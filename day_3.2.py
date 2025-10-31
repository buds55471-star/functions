# Write a function that calculates the factorial of a number
def factorial(n):
    i = 1
    product = 1
    while i<=n:
        product = product*i
        i+=1
    print(f"The factorial of number {n} is {product}")
factorial(5)
factorial(7)

