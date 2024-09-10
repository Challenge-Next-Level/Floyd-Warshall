from collections import defaultdict
def solution(genres, plays):
    genre_dict = defaultdict(list)
    genre_play_dict = defaultdict(int)
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        genre_dict[genre].append([play, -1 * i])
        genre_play_dict[genre] += play

    genre_play_list = list()
    for key, value in genre_play_dict.items():
        genre_play_list.append([value, key])
    genre_play_list.sort(reverse=True)

    answer = []
    for p, g in genre_play_list:
        g_p = genre_dict[g]
        g_p.sort(reverse=True)
        answer.append(-1 * g_p[0][1])
        if len(g_p) >= 2:
            answer.append(-1 * g_p[1][1])

    return answer
