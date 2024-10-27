N, M, L, K = map(int, input().split())
star_list = [list(map(int, input().split())) for _ in range(K)]

answer = K

for star_a_x, star_a_y in star_list:
    for star_b_x, star_b_y in star_list:
        star_count = 0
        # [star_a_x, star_b_y] 위치에 트램펄린 설치
        for star_c_x, star_c_y in star_list:
            if star_a_x <= star_c_x and star_c_x <= star_a_x + L and star_b_y <= star_c_y and star_c_y <= star_b_y + L:
                star_count += 1

        answer = min(answer, K - star_count)

print(answer)