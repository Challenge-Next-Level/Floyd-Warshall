text = list(input())

visited = [False for _ in range(len(text))]
answer = ['Z' * i for i in range(len(text) + 1)]


def s(_t, _v, _l):
    if _l > 0:
        answer_text = answer[_l]
        now_text = "".join(_t)
        if now_text <= answer_text:
            answer[_l] = now_text

    for idx in range(len(text)):
        if not _v[idx]:
            _v[idx] = True
            _t[idx] = text[idx]
            s(_t, _v, _l + 1)
            _v[idx] = False
            _t[idx] = ''


s(["" for _ in range(len(text))], visited, 0)

for a in answer[1:]:
    print("".join(a))
