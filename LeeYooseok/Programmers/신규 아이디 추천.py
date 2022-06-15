def solution(new_id):
    new_id = new_id.lower()

    new_new_id = ""
    for s in new_id:
        if s.isalpha() or s.isdigit() or s == "-" or s == "_" or s == ".":
            new_new_id += s
    new_id = new_new_id

    flag = False
    new_new_id = ""
    for s in new_id:
        if not flag:
            new_new_id += s
            if s == ".":
                flag = True
        else:
            if s != ".":
                flag = False
                new_new_id += s
            else:
                continue
    new_id = new_new_id

    if new_id != "":
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id != "":
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    if new_id == "":
        new_id = "a"


    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == ".":
        new_id = new_id[:-1]

    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    print(new_id)

solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")
