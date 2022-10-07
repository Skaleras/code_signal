def solution(m):
    # m is the matrix
    r = len(m) #number of rows
    c = len(m[0]) #number of columns
    
    total = 0
    # i position in x, j position in y
    for j in range(c):
        for i in range(r):
            if m[i][j]!=0:
                total+=m[i][j]
            else:
                break
    return total