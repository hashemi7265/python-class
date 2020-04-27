#1: Write a Python program to count the number of lines in a text file

linea=[]
empty_line_count=0
with open('test.txt', 'r')as fd:
    for line in fd:
        if line=='/n':
            empty_line_count += 1
        else:
            line.append(line)
print("empty line count :", empty_line_count)
print("List of lined :", line )
