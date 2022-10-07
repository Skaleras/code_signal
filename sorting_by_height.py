def solution(a):
    
    #This function sorts any number of heights and ignores -1's
    non_trees_array = []
    for pos, i in enumerate(a):
        if i != -1:
            non_trees_array.append((i, pos))
            #(pos, i) or (i, pos) testing
    non_trees_array.sort()
    #print(non_trees_array)
    
    heights = []
    for i in non_trees_array:
        heights.append(i[0])
    #print(heights)
    
    trees_positions = []
    for pos, i in enumerate(a):
        if i == -1:
            trees_positions.append((i, pos))
    
    #print(trees_positions)
    for i, pos in trees_positions:
        heights.insert(pos, i)
    
    return heights