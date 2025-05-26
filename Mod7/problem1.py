#1. Write a function called count_vowels(input) that takes a string and returns the number of vowels (a, e, i, o, u) in it.

sentance = ""
vowels = ["a", "e", "i", "o", "u"]

def count_vowels(sentance):
    vowel_total = 0
    lower_sentance = sentance.lower()
    for i in range(len(lower_sentance)):
        if vowels[0] in lower_sentance[i]:
            vowel_total += 1
        if vowels[1] in lower_sentance[i]:
            vowel_total += 1
        if vowels[2] in lower_sentance[i]:
            vowel_total += 1
        if vowels[3] in lower_sentance[i]:
            vowel_total += 1
        if vowels[4] in lower_sentance[i]:
            vowel_total += 1
    return print(vowel_total)

count_vowels(input("What sentance will you use? "))
