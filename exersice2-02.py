# 2: write python program to add two matrix with same dimensions

def addTwoMatrix(x, y):
    res = []
    for i in range(len(y)):
        row = []
        for j in range(len(y[0])):
            row.append(y[i][j]+x[i][j])
        res.append(row)
    return res

print(addTwoMatrix([[1,2,3], [4 ,5,6]],[[1,2,3], [4 ,5,6]] ))