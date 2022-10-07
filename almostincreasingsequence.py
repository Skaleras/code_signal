def solution(sequence):
    droppped = False
    last = prev = min(sequence) - 1

    #element stands for current element being seen, 
    #last for last element seen and prev for previous element seen
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True