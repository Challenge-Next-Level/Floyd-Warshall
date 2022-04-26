n = int(input())

short_cuts = set()

for _ in range(n):
    words = list(input().split())
    flag = False

    # 각 단어 앞자리 확인
    for w in words:
        if w[0].upper() not in short_cuts:
            short_cuts.add(w[0].upper())
            result = " ".join(words)
            idx = result.find(w[0])
            print(result[:idx] + "[" + w[0] + "]" + result[idx+1:])
            flag = True
            break

    second_flag = False
    if not flag:
        # 전체 단어 확인
        for w in words:
            if second_flag:
                break
            for each_w in w[1:]:
                if each_w.upper() not in short_cuts:
                    short_cuts.add(each_w.upper())
                    result = " ".join(words)
                    idx = result.find(each_w)
                    print(result[:idx] + "[" + each_w + "]" + result[idx+1:])
                    second_flag = True
                    break

    if not flag and not second_flag:
        print(" ".join(words))

