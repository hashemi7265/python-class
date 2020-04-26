# 1: write python program to transpose given matrix


def transpose(a):
    result = [[[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]]
    for row in result:
        return row

print("result=",transpose([[10, 30, 50], [20, 40, 60]]))
print("result=",transpose([[1, 1, 1], [3, 3, 3], [5, 5, 5],[7, 7, 7]]))
print("result=",transpose([[5, 10, 15]]))
