# Create a function multiply(*args) that multiplies all given numbers.

def multiple(*nums):
    mul = 1
    for num in nums:
        mul = mul*num
    return mul

print(multiple(2,3,4))


