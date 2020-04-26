#3. Write a Python program to count the occurrences of each word in a given sentence
import string

text = "Mango- banana, Apple! pear Mango!"

dic = {}

text = text.translate(text.maketrans("", "", string.punctuation))
text = text.strip()
text = text.lower()
text = text.split(" ")

for word in text:
  if word in dic:
    dic[word] = dic[word] + 1
  else:
    dic[word] = 1

print(dic)