def solution(friends, gifts):
    friends_dict = dict()
    for idx in range(len(friends)):
        friends_dict[friends[idx]] = [idx, 0, [0 for _ in range(len(friends))]]

    for gift in gifts:
        sender, receiver = gift.split()
        receiver_idx = friends_dict[receiver][0]

        friends_dict[sender][1] += 1
        friends_dict[sender][2][receiver_idx] += 1

        friends_dict[receiver][1] -= 1

    gift_count = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            # i, j 비교

            # i -> j
            i_j = friends_dict[friends[i]][2][j]
            # j -> i
            j_i = friends_dict[friends[j]][2][i]

            if i_j > j_i:
                gift_count[i] += 1
            elif i_j < j_i:
                gift_count[j] += 1
            else:
                if friends_dict[friends[i]][1] > friends_dict[friends[j]][1]:
                    gift_count[i] += 1
                elif friends_dict[friends[i]][1] < friends_dict[friends[j]][1]:
                    gift_count[j] += 1

    print(max(gift_count))