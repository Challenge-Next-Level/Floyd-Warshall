N = int(input())

option_list = [input() for _ in range(N)]

short_cut_set = set()

for option in option_list:
    flag = False
    word_list = option.split()

    # 각 단어의 앞자리 확인
    for i in range(len(word_list)):
        word = word_list[i]
        if word[0].upper() not in short_cut_set:
            short_cut_set.add(word[0].upper())

            word_list[i] = "[" + word_list[i][0] + "]" + word_list[i][1:]
            print(" ".join(word_list))
            flag = True
            break

    second_flag = False
    if not flag:
        # 전체 단어 확인
        for word in word_list:
            if second_flag:
                break
            for char in word[1:]:
                if char.upper() not in short_cut_set:
                    short_cut_set.add(char.upper())

                    result = " ".join(word_list)
                    idx = result.find(char)
                    print(result[:idx] + "[" + char + "]" + result[idx + 1:])
                    second_flag = True
                    break

    if not flag and not second_flag:
        print(option)
