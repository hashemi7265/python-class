#1. Write a Python program to count the number of characters (character frequency) in a string

word = "google.com'"
characterFrequency = {}
for i in word:
    if i in characterFrequency:
        characterFrequency[i] += 1
    else:
        characterFrequency[i] = 1
print ("Count of all characters in word is :\n " +  str(characterFrequency))