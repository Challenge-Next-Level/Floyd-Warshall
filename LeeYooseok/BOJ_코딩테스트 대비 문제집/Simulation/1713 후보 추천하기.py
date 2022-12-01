N = int(input())
T = int(input())

# dict - key : 학생 번호, value : [추천 수, 들어온 순서]

student_num_list = list(map(int, input().split()))
candidate_dict = dict()

for t in range(T):
    student_num = student_num_list[t]
    # 추천받은 학생이 사진 틀에 있다면,
    if student_num in candidate_dict.keys():
        old_num, old_order = candidate_dict[student_num]
        candidate_dict[student_num] = [old_num + 1, old_order] # 이미 추천 받은 사람이 또 추천 받을 경우, 추천 받은 순서를 갱신하면 X
    # 추천 받은 학생이 사진 틀에 없다면,
    else:
        # 사진 틀이 꽉 안찬 상태
        if len(list(candidate_dict.keys())) < N:
            candidate_dict[student_num] = [1, t + 1]
        # 사진 틀이 꽉 찬 상태
        else:
            # value 의 추천수, 들어온 순서 대로 key 를 정렬 하여, 가장 앞 학생 pop
            removed_student = sorted(candidate_dict.items(), key = lambda x: (x[1][0], x[1][1])).pop(0)
            candidate_dict.pop(removed_student[0])

            # 새로 들어오는 학생 추가
            candidate_dict[student_num] = [1, t + 1]

print(" ".join(list(map(str, sorted(candidate_dict.keys())))))