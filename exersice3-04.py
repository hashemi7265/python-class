#write a function to generate a dictionary that contains (i, i*i)
#	input 9
#	output :{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def func(i):
  output = dict()
  for v in range(1,i):
      output[v] = v * v
  return output


print(func(9))