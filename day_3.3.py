# Create a function that finds the largest number in a list (without using max())

def larger(n):
    # Assume the first number is the largest
    largest = n[0]

    # Loop through the rest of the list
    for i in n:
        if i > largest:
            largest = i  # Update largest if current number is bigger

    return largest

# Example
numbers = [3, 7, 2, 9, 5]
print("The largest number is:", larger( numbers ))

