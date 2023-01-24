def solution(grid):
    import numpy
    #You should check the solution for 3 major cases:
    #   There aren't repeated elements in each row
    #   There aren't repeated elements in each column
    #   There aren't repeated elements in each 3x3 sub-grid
    #   to avoid over iteration you can simply stop the program when you see a repeated 
    #   number in rows, columns or 3x3 sub-grids
    
    #let's check if the rows are valid
    for row in grid:
        numbers = set(row)
        if len(numbers) < 9:
            return False
        else:
            pass
    
    #let's check if the columns are valid
    t_grid = numpy.transpose(grid)
    for row in t_grid:
        numbers = set(row)
        if len(numbers) < 9:
            return False
        else:
            pass
            
    #Let's check if the subgrids are valid
    def g(x,y):
        return sorted([grid[i][j] for i in range(x,x+3) for j in range(y,y+3)]) != list(range(1,10))
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            if g(i,j):
                return False
    return True
