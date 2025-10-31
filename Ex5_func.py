#Write a function even_or_odd(num) that returns "Even" if the number is even,
# otherwise "Odd".

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(6))

