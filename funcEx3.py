'''Write a function called add_all_nums which takes arbitrary number of
arguments and sums all the arguments. Check if all the list items are number types.
If not do give a reasonable feedback.'''

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        sum+=num
    return sum


print(add_all_nums(1,2,3,4,5))

