import sys

input = sys.stdin.readline

vowel = {"a", "e", "i", "o", "u"}

while True:
    word = input().rstrip()

    if word == "end":
        break

    condition_1 = False
    condition_2 = True
    condition_3 = True

    for char_index in range(len(word)):
        now_char = word[char_index]
        if not condition_1 and now_char in vowel:
            condition_1 = True

        if condition_2 and char_index < (len(word) - 1):
            if now_char != "e" and now_char != "o":
                if now_char == word[char_index + 1]:
                    condition_2 = False

        if condition_3 and char_index < (len(word) - 2):
            vowel_cnt = 0
            for i in range(3):
                if word[char_index + i] in vowel:
                    vowel_cnt += 1

            if vowel_cnt == 0 or vowel_cnt == 3:
                condition_3 = False

    if condition_1 and condition_2 and condition_3:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
