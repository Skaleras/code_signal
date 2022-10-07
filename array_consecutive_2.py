def solution(statues):
    statues = sorted(statues)
    #print(statues)
    highest_statue = statues[-1]
    lowest_statue = statues[0]
    #print(range(lowest_statue, highest_statue))
    missing_statues = []
    for i in range(lowest_statue, highest_statue):
        if i not in statues:
            missing_statues.append(i)
    return len(missing_statues)