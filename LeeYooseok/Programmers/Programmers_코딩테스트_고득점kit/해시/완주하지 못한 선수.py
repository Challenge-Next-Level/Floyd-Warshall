from collections import defaultdict

def solution(participant, completion):
    participant_dict = defaultdict(int)
    for p in participant:
        participant_dict[p] += 1

    for c in completion:
        participant_dict[c] -= 1

    for key, value in participant_dict.items():
        if value > 0:
            return key