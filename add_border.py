def solution(picture):
    matrix = list()
    x = len(picture[0])
    y = len(picture)
    new_matrix_x = x+2
    matrix.append('*'*new_matrix_x)
    for i in picture:
        i = '*' + i + '*'
        matrix.append(i)
    matrix.append('*'*new_matrix_x)
    #print(matrix)
    return matrix