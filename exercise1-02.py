#2. Write a Python program to remove the characters which have odd index values of a given string

def oddValuesString(str):
  carac = ""
  for a in range(len(str)):
    if a % 4 == 0:
      carac += str[a]
  return carac

print(oddValuesString('computer pasargad'))
