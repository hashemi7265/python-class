#3- Write a recursive function which can compute the factorial of a given numbers.
def fact (n):
  if n == 0: return 1
  else : return (n * fact(n-1))
print(fact(10))
