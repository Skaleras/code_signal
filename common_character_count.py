def solution(s1, s2):
    common_chars = []
    #print(s1, set(s1))
    for i in set(s1):
        common_chars.append(min(s1.count(i), s2.count(i)))
        #print(common_chars)
    return sum(common_chars)

solution('aabcc', 'adcaa')