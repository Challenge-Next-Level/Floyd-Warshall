P = int(input())

for _ in range(P):
    unsorted_student_list = list(map(int, input().split()))
    P = unsorted_student_list.pop(0)

    answer = 0
    sorted_student_list = [unsorted_student_list[0]]

    for i in range(1, 20):
        student = unsorted_student_list[i]

        if sorted_student_list[-1] < student:
            sorted_student_list.append(student)
        else:
            student_index = 0
            left, right = 0, i

            while left <= right:
                mid = (left + right) // 2

                if sorted_student_list[mid] < student:
                    left = mid + 1
                else:
                    right = mid - 1
                    student_index = mid

            sorted_student_list.insert(student_index, student)
            answer += (i - student_index)

    print(P, answer)