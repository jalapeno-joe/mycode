#!/usr/bin/env python3

words = ["cat", "dog", "beaver", "quasimodo"]
vowels = ["a", "e", "i", "o", "u", "y"]
blankv = []
blankc = []
fullv = []
fullc = []
wordv = 0
wordc = 0
cons = 0
vow = 0

for item in words:
    print(item)
    blankv = []
    blankc = []
    for letter in item:
        if letter in vowels:
            blankv.append(letter)
            fullv.append(letter)
#            vow = vow + 1
            wordv += 1
        else:
            blankc.append(letter)
            fullc.append(letter)
#            cons = cons + 1
            wordc += 1
    print("vowels:", wordv, blankv, "Consonants", wordc, blankc)
#print("vowels", vow, fullv, "consonants", cons, fullc)
#print("vowles", vow, "constants", cons)
print("vowles", wordv, "constand", wordc)


