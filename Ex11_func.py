'''Define a function count_vowels(s) that counts
and returns the number of vowels in a string. '''

def count_vowels(s):
    total = 0
    vowels = "aeiou"
    for vowel in vowels:
        if vowel in s:
            total+=1
    return total

print(count_vowels("Hello"))
