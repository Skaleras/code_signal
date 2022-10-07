def solution(inputString):
    answer = ''
    do_not_reverse_this = ''
    
    for index, i in enumerate(inputString):
        if i.isalpha():
            do_not_reverse_this = do_not_reverse_this + i
        elif i == '(':
            starting_parenthesis = inputString[index+1] #toma el inicio del string quieres voltear
            starting_index = index+1
        elif i == ')':
            closed_string = inputString[starting_index:index] #toma el string que esta entre parentesis
            new_string = closed_string[::-1]  #voltea el string example: 'bar' se convierte en 'rab'
            answer = answer + new_string
    return answer