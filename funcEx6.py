'''Declare a function named sum_of_odds.
It takes a number parameter and it adds all the odd numbers in that range. '''

def sum_of_odds(nums):
    sum = 0
    for num in nums:
        if num%2!=0:
            sum+=num
    print(sum)

nums = [1,5,8,6,9]
sum_of_odds(nums)

