def solution(a):
    team_a = []
    team_b = []
    for index, i in enumerate(a, start=1):
        if index % 2 != 0:
            team_a.append(i)
        else:
            team_b.append(i)

    return [sum(team_a), sum(team_b)]