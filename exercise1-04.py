#4. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form

a = input("input : ")

words = [word for word in a.split("-")]

print( "-".join(sorted(list(set(words)))))
