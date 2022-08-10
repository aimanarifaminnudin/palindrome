# Exercise 5
# Aiman

a = str(input('Enter word: '))
word = a.upper()
reverseWord = a.upper()

if reverseWord == word[::-1] :
    print('Palindrome')
else :
    print('Not a Palindrome')