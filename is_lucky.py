def solution(n):
    
    #this function tells you if a given number is lucky or not
    number_in_str = str(n)
    number_of_digits = len(number_in_str)
    
    position_1 = int(number_of_digits/2)
    #print(position_1)
    position_2 = int(number_of_digits/2)
    #print(position_2)
    
    first_half = number_in_str[:position_1]
    second_half = number_in_str[position_2:]

    total_1 = 0
    for i in first_half:
        total_1 = int(i) + total_1
        
    total_2 = 0
    for j in second_half:
        total_2 = int(j) + total_2
        
    if total_1 == total_2:
        return True
    else:
        return False