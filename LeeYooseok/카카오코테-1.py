def solution(survey, choices):
    types = {
        'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0
    }
    for i in range(len(survey)):
        s, c = survey[i], choices[i]
        if c <= 3:
            if c == 1:
                score = 3
            elif c == 2:
                score = 2
            else:
                score = 1
            types[s[0]] += score
        elif c >= 5:
            if c == 5:
                score = 1
            elif c == 6:
                score = 2
            else:
                score = 3
            types[s[1]] += score

    answer = ''

    # R / T
    if types['R'] >= types['T']:
        answer += 'R'
    else:
        answer += 'T'

    # C / F
    if types['C'] >= types['F']:
        answer += 'C'
    else:
        answer += 'F'

    # J / M
    if types['J'] >= types['M']:
        answer += 'J'
    else:
        answer += 'M'

    # A / N
    if types['A'] >= types['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer