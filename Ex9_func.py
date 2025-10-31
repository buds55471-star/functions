'''Write a function sum_list(lst) that takes a list of numbers and
returns their sum (without using sum()).'''

def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
