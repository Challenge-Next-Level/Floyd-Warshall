from collections import defaultdict

N, M = map(int, input().split())
song_dict = defaultdict(list)
for _ in range(N):
    user_input = list(input().split())
    T = user_input.pop(0)
    S = user_input.pop(0)
    song_dict["".join(user_input[:3])].append(S)

for _ in range(M):
    user_input = "".join(list(input().split()))

    if user_input in song_dict.keys():
        if len(song_dict[user_input]) >= 2:
            print("?")
        else:
            print(song_dict[user_input][0])
    else:
        print("!")