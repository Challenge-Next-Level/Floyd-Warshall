text = input()

len_text = len(text)

mid = (len_text // 2) - 1

if len_text <= 1:
    print(len_text)
else:
    while mid < len_text:
        right = text[mid+1:]
        len_right = len(right)
        sub_left = text[mid-len_right:mid]
        sub_left2 = sub_left[1:] + text[mid]

        if right == sub_left[::-1]:
            print(len_text + mid-len_right)
            break
        elif right == sub_left2[::-1]:
            print(len_text + mid-len_right + 1)
            break
        else:
            mid += 1