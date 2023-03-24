from collections import defaultdict

N = int(input())
str_list = input()
len_str = len(str_list)

start, end = 0, 1
answer = 1

text_dict = defaultdict(int)
text_dict[str_list[start]] = 1

if len_str == 1:
    print(1)
elif len(set(str_list)):
    print(len(str_list))
else:
    while start < end and end < len_str:
        alpha_cnt = len(list(text_dict.keys()))
        text_len = (end - start)

        if alpha_cnt <= N:
            answer = max(answer, end - start)

            if end < len_str:
                end += 1
                text_dict[str_list[end - 1]] += 1

        else:
            if text_dict[str_list[start]] > 1:
                text_dict[str_list[start]] -= 1
            else:
                text_dict.pop(str_list[start])
            start += 1

    print(answer)